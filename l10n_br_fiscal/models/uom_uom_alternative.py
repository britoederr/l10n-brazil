# Copyright 2019 KMEE INFORMATICA LTDA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class UomUomAlternative(models.Model):
    _name = "uom.uom.alternative"
    _rec_name = "code"

    code = fields.Char(string="Code")

    uom_id = fields.Many2one(comodel_name="uom.uom")

    _sql_constraints = [
        (
            "uom_alternative_unique",
            "UNIQUE(code, uom_id)",
            "You can note repeat the alternative name",
        )
    ]
