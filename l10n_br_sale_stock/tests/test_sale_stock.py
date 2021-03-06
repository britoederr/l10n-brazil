# Copyright 2020 KMEE
# Copyright (C) 2021  Magno Costa - Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestSaleStock(TransactionCase):

    def setUp(self):
        super().setUp()
        self.invoice_model = self.env['account.invoice']
        self.invoice_wizard = self.env['stock.invoice.onshipping']

    def test_02_sale_stock_return(self):
        """
        Test a SO with a product invoiced on delivery. Deliver and invoice
        the SO, then do a return
        of the picking. Check that a refund invoice is well generated.
        """
        # intial so
        self.partner = self.env.ref('l10n_br_base.res_partner_address_ak2')
        self.product = self.env.ref('product.product_delivery_01')
        so_vals = {
            'partner_id': self.partner.id,
            'partner_invoice_id': self.partner.id,
            'partner_shipping_id': self.partner.id,
            'order_line': [(0, 0, {
                'name': self.product.name,
                'product_id': self.product.id,
                'product_uom_qty': 3.0,
                'product_uom': self.product.uom_id.id,
                'price_unit': self.product.list_price
                })],
            'pricelist_id': self.env.ref('product.list0').id,
            }
        self.so = self.env['sale.order'].create(so_vals)

        for line in self.so.order_line:
            line._onchange_product_id_fiscal()

        # confirm our standard so, check the picking
        self.so.action_confirm()
        self.assertTrue(self.so.picking_ids,
                        'Sale Stock: no picking created for "invoice on '
                        'delivery" storable products')

        # set stock.picking to be invoiced
        self.assertTrue(len(self.so.picking_ids) == 1, 'More than one stock '
                                                       'picking for sale.order')
        self.so.picking_ids.set_to_be_invoiced()

        # validate stock.picking
        stock_picking = self.so.picking_ids
        self.env['stock.immediate.transfer'].create(
            {'pick_ids': [(4, stock_picking.id)]}).process()

        # compare sale.order.line with stock.move
        stock_move = stock_picking.move_lines
        sale_order_line = self.so.order_line

        sm_fields = [key for key in self.env['stock.move']._fields.keys()]
        sol_fields = [key for key in self.env[
            'sale.order.line']._fields.keys()]

        skipped_fields = [
            'id',
            'display_name',
            'state',
            ]
        common_fields = list(set(sm_fields) & set(sol_fields) - set(
            skipped_fields))

        for field in common_fields:
            self.assertEqual(stock_move[field],
                             sale_order_line[field],
                             'Field %s failed to transfer from '
                             'sale.order.line to stock.move' % field)

    def test_picking_sale_order_product_and_service(self):
        """
        Test Sale Order with product and service
        """

        sale_order_2 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_2')
        sale_order_2.action_confirm()
        picking = sale_order_2.picking_ids
        # Check product availability
        picking.action_assign()
        # Apenas o Produto criado
        self.assertEqual(len(picking.move_ids_without_package), 1)
        # Force product availability
        for move in picking.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking.button_validate()
        self.assertEqual(picking.state, 'done')
        wizard_obj = self.invoice_wizard.with_context(
            active_ids=picking.ids,
            active_model=picking._name,
            active_id=picking.id,
        )
        fields_list = wizard_obj.fields_get().keys()
        wizard_values = wizard_obj.default_get(fields_list)
        wizard = wizard_obj.create(wizard_values)
        wizard.onchange_group()
        wizard.action_generate()
        domain = [('picking_ids', '=', picking.id)]
        invoice = self.invoice_model.search(domain)
        self.assertEqual(picking.invoice_state, 'invoiced')
        self.assertIn(invoice, picking.invoice_ids)
        self.assertIn(picking, invoice.picking_ids)
        # Picking criado com o Partner Shipping da Sale Order
        self.assertEqual(picking.partner_id, sale_order_2.partner_shipping_id)
        # Fatura criada com o Partner Invoice da Sale Order
        self.assertEqual(invoice.partner_id, sale_order_2.partner_invoice_id)
        # Fatura criada com o Partner Shipping usado no Picking
        self.assertEqual(invoice.partner_shipping_id, picking.partner_id)
        # Quando informado usar o Termo de Pagto definido no Pedido de Venda
        # e não o padrão do cliente
        self.assertEqual(
            invoice.payment_term_id, sale_order_2.payment_term_id)

        # Apenas a Fatura com a linha do produto foi criada
        self.assertEqual(len(invoice.invoice_line_ids), 1)

    def test_picking_invoicing_partner_shipping_invoiced(self):
        """
        Test the invoice generation grouped by partner/product with 2
        picking and 3 moves per picking, but Partner to Shipping is
        different from Partner to Invoice.
        """
        sale_order_1 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_1')
        sale_order_1.action_confirm()
        picking = sale_order_1.picking_ids
        picking.action_confirm()
        # Check product availability
        picking.action_assign()
        # Force product availability
        for move in picking.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking.button_validate()

        sale_order_2 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_2')
        sale_order_2.action_confirm()
        picking2 = sale_order_2.picking_ids
        # Check product availability
        picking2.action_assign()
        # Force product availability
        for move in picking2.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking2.button_validate()
        self.assertEqual(picking.state, 'done')
        self.assertEqual(picking2.state, 'done')
        pickings = picking | picking2
        wizard_obj = self.invoice_wizard.with_context(
            active_ids=pickings.ids,
            active_model=pickings._name,
        )
        fields_list = wizard_obj.fields_get().keys()
        wizard_values = wizard_obj.default_get(fields_list)
        # One invoice per partner but group products
        wizard_values.update({
            'group': 'partner_product',
        })
        wizard = wizard_obj.create(wizard_values)
        wizard.onchange_group()
        wizard.action_generate()
        domain = [('picking_ids', 'in', (picking.id, picking2.id))]
        invoice = self.invoice_model.search(domain)
        # Fatura Agrupada
        self.assertEquals(len(invoice), 1)
        self.assertEqual(picking.invoice_state, 'invoiced')
        self.assertEqual(picking2.invoice_state, 'invoiced')
        # Fatura deverá ser criada com o partner_invoice_id
        self.assertEqual(
            invoice.partner_id, sale_order_1.partner_invoice_id)
        # Fatura com o partner shipping
        self.assertEqual(
            invoice.partner_shipping_id, picking.partner_id)
        self.assertIn(invoice, picking.invoice_ids)
        self.assertIn(picking, invoice.picking_ids)
        self.assertIn(invoice, picking2.invoice_ids)
        self.assertIn(picking2, invoice.picking_ids)

        # Not grouping products with different sale line,
        # 3 products from sale_order_1 and 1 product from sale_order_2
        self.assertEquals(len(invoice.invoice_line_ids), 4)
        for inv_line in invoice.invoice_line_ids:
            self.assertTrue(
                inv_line.invoice_line_tax_ids,
                'Error to map Sale Tax in invoice.line.')

    def test_ungrouping_pickings_partner_shipping_different(self):
        """
        Test the invoice generation grouped by partner/product with 3
        picking and 3 moves per picking, the 3 has the same Partner to
        Invoice but one has Partner to Shipping so shouldn't be grouping.
        """

        sale_order_1 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_1')
        sale_order_1.action_confirm()
        picking = sale_order_1.picking_ids
        picking.action_confirm()
        # Check product availability
        picking.action_assign()
        # Force product availability
        for move in picking.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking.button_validate()

        sale_order_3 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_3')
        sale_order_3.action_confirm()
        picking3 = sale_order_3.picking_ids
        # Check product availability
        picking3.action_assign()
        # Force product availability
        for move in picking3.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking3.button_validate()
        self.assertEqual(picking.state, 'done')
        self.assertEqual(picking3.state, 'done')

        sale_order_4 = self.env.ref(
            'l10n_br_sale_stock.main_so_l10n_br_sale_stock_4')
        sale_order_4.action_confirm()
        picking4 = sale_order_4.picking_ids
        # Check product availability
        picking4.action_assign()
        # Force product availability
        for move in picking4.move_ids_without_package:
            move.quantity_done = move.product_uom_qty
        picking4.button_validate()
        self.assertEqual(picking.state, 'done')
        self.assertEqual(picking3.state, 'done')

        pickings = picking | picking3 | picking4
        wizard_obj = self.invoice_wizard.with_context(
            active_ids=pickings.ids,
            active_model=pickings._name,
        )
        fields_list = wizard_obj.fields_get().keys()
        wizard_values = wizard_obj.default_get(fields_list)
        # One invoice per partner but group products
        wizard_values.update({
            'group': 'partner_product',
        })
        wizard = wizard_obj.create(wizard_values)
        wizard.onchange_group()
        wizard.action_generate()
        domain = [(
            'picking_ids', 'in', (picking.id, picking3.id, picking4.id))]
        invoices = self.invoice_model.search(domain)
        # Mesmo tendo o mesmo Partner Invoice se não tiver o
        # mesmo Partner Shipping não deve ser Agrupado
        self.assertEquals(len(invoices), 2)
        self.assertEqual(picking.invoice_state, 'invoiced')
        self.assertEqual(picking3.invoice_state, 'invoiced')
        self.assertEqual(picking4.invoice_state, 'invoiced')

        # Fatura que tem um Partner shipping
        # diferente não foi agrupada
        invoice_pick_1 = invoices.filtered(
            lambda t: t.partner_shipping_id == picking.partner_id)
        # Fatura deverá ser criada com o partner_invoice_id
        self.assertEqual(
            invoice_pick_1.partner_id, sale_order_1.partner_invoice_id)
        # Fatura criada com o Partner Shipping usado no Picking
        self.assertEqual(
            invoice_pick_1.partner_shipping_id, picking.partner_id)

        # Fatura Agrupada, não deve ter o partner_shipping_id preenchido
        invoice_pick_3_4 = invoices.filtered(
            lambda t: not t.partner_shipping_id)
        self.assertIn(invoice_pick_3_4, picking3.invoice_ids)
        self.assertIn(invoice_pick_3_4, picking4.invoice_ids)
