# -*- coding: utf-8 -*-
# Copyright 2018 KMEE INFORMATICA LTDA - Luis Felipe Mileo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

_xmlid_renames = [
    ('l10n_br_base.br_ac', 'base.state_br_ac'),
    ('l10n_br_base.br_al', 'base.state_br_al'),
    ('l10n_br_base.br_am', 'base.state_br_am'),
    ('l10n_br_base.br_ap', 'base.state_br_ap'),
    ('l10n_br_base.br_ba', 'base.state_br_ba'),
    ('l10n_br_base.br_ce', 'base.state_br_ce'),
    ('l10n_br_base.br_df', 'base.state_br_df'),
    ('l10n_br_base.br_es', 'base.state_br_es'),
    ('l10n_br_base.br_go', 'base.state_br_go'),
    ('l10n_br_base.br_ma', 'base.state_br_ma'),
    ('l10n_br_base.br_mg', 'base.state_br_mg'),
    ('l10n_br_base.br_ms', 'base.state_br_ms'),
    ('l10n_br_base.br_mt', 'base.state_br_mt'),
    ('l10n_br_base.br_pa', 'base.state_br_pa'),
    ('l10n_br_base.br_pb', 'base.state_br_pb'),
    ('l10n_br_base.br_pe', 'base.state_br_pe'),
    ('l10n_br_base.br_pi', 'base.state_br_pi'),
    ('l10n_br_base.br_pr', 'base.state_br_pr'),
    ('l10n_br_base.br_rj', 'base.state_br_rj'),
    ('l10n_br_base.br_rn', 'base.state_br_rn'),
    ('l10n_br_base.br_ro', 'base.state_br_ro'),
    ('l10n_br_base.br_rr', 'base.state_br_rr'),
    ('l10n_br_base.br_rs', 'base.state_br_rs'),
    ('l10n_br_base.br_sc', 'base.state_br_sc'),
    ('l10n_br_base.br_se', 'base.state_br_se'),
    ('l10n_br_base.br_sp', 'base.state_br_sp'),
    ('l10n_br_base.br_to', 'base.state_br_to'),
    ('l10n_br_data_base.res_bank_1', 'l10n_br_base.res_bank_1'),
    ('l10n_br_data_base.res_bank_2', 'l10n_br_base.res_bank_2'),
    ('l10n_br_data_base.res_bank_3', 'l10n_br_base.res_bank_3'),
    ('l10n_br_data_base.res_bank_4', 'l10n_br_base.res_bank_4'),
    ('l10n_br_data_base.res_bank_5', 'l10n_br_base.res_bank_5'),
    ('l10n_br_data_base.res_bank_6', 'l10n_br_base.res_bank_6'),
    ('l10n_br_data_base.res_bank_7', 'l10n_br_base.res_bank_7'),
    ('l10n_br_data_base.res_bank_8', 'l10n_br_base.res_bank_8'),
    ('l10n_br_data_base.res_bank_9', 'l10n_br_base.res_bank_9'),
    ('l10n_br_data_base.res_bank_10', 'l10n_br_base.res_bank_10'),
    ('l10n_br_data_base.res_bank_11', 'l10n_br_base.res_bank_11'),
    ('l10n_br_data_base.res_bank_12', 'l10n_br_base.res_bank_12'),
    ('l10n_br_data_base.res_bank_13', 'l10n_br_base.res_bank_13'),
    ('l10n_br_data_base.res_bank_14', 'l10n_br_base.res_bank_14'),
    ('l10n_br_data_base.res_bank_15', 'l10n_br_base.res_bank_15'),
    ('l10n_br_data_base.res_bank_16', 'l10n_br_base.res_bank_16'),
    ('l10n_br_data_base.res_bank_17', 'l10n_br_base.res_bank_17'),
    ('l10n_br_data_base.res_bank_18', 'l10n_br_base.res_bank_18'),
    ('l10n_br_data_base.res_bank_19', 'l10n_br_base.res_bank_19'),
    ('l10n_br_data_base.res_bank_20', 'l10n_br_base.res_bank_20'),
    ('l10n_br_data_base.res_bank_21', 'l10n_br_base.res_bank_21'),
    ('l10n_br_data_base.res_bank_22', 'l10n_br_base.res_bank_22'),
    ('l10n_br_data_base.res_bank_23', 'l10n_br_base.res_bank_23'),
    ('l10n_br_data_base.res_bank_24', 'l10n_br_base.res_bank_24'),
    ('l10n_br_data_base.res_bank_25', 'l10n_br_base.res_bank_25'),
    ('l10n_br_data_base.res_bank_26', 'l10n_br_base.res_bank_26'),
    ('l10n_br_data_base.res_bank_27', 'l10n_br_base.res_bank_27'),
    ('l10n_br_data_base.res_bank_28', 'l10n_br_base.res_bank_28'),
    ('l10n_br_data_base.res_bank_29', 'l10n_br_base.res_bank_29'),
    ('l10n_br_data_base.res_bank_30', 'l10n_br_base.res_bank_30'),
    ('l10n_br_data_base.res_bank_31', 'l10n_br_base.res_bank_31'),
    ('l10n_br_data_base.res_bank_32', 'l10n_br_base.res_bank_32'),
    ('l10n_br_data_base.res_bank_33', 'l10n_br_base.res_bank_33'),
    ('l10n_br_data_base.res_bank_34', 'l10n_br_base.res_bank_34'),
    ('l10n_br_data_base.res_bank_35', 'l10n_br_base.res_bank_35'),
    ('l10n_br_data_base.res_bank_36', 'l10n_br_base.res_bank_36'),
    ('l10n_br_data_base.res_bank_37', 'l10n_br_base.res_bank_37'),
    ('l10n_br_data_base.res_bank_38', 'l10n_br_base.res_bank_38'),
    ('l10n_br_data_base.res_bank_39', 'l10n_br_base.res_bank_39'),
    ('l10n_br_data_base.res_bank_40', 'l10n_br_base.res_bank_40'),
    ('l10n_br_data_base.res_bank_41', 'l10n_br_base.res_bank_41'),
    ('l10n_br_data_base.res_bank_42', 'l10n_br_base.res_bank_42'),
    ('l10n_br_data_base.res_bank_43', 'l10n_br_base.res_bank_43'),
    ('l10n_br_data_base.res_bank_44', 'l10n_br_base.res_bank_44'),
    ('l10n_br_data_base.res_bank_45', 'l10n_br_base.res_bank_45'),
    ('l10n_br_data_base.res_bank_46', 'l10n_br_base.res_bank_46'),
    ('l10n_br_data_base.res_bank_47', 'l10n_br_base.res_bank_47'),
    ('l10n_br_data_base.res_bank_48', 'l10n_br_base.res_bank_48'),
    ('l10n_br_data_base.res_bank_49', 'l10n_br_base.res_bank_49'),
    ('l10n_br_data_base.res_bank_50', 'l10n_br_base.res_bank_50'),
    ('l10n_br_data_base.res_bank_51', 'l10n_br_base.res_bank_51'),
    ('l10n_br_data_base.res_bank_52', 'l10n_br_base.res_bank_52'),
    ('l10n_br_data_base.res_bank_53', 'l10n_br_base.res_bank_53'),
    ('l10n_br_data_base.res_bank_54', 'l10n_br_base.res_bank_54'),
    ('l10n_br_data_base.res_bank_55', 'l10n_br_base.res_bank_55'),
    ('l10n_br_data_base.res_bank_56', 'l10n_br_base.res_bank_56'),
    ('l10n_br_data_base.res_bank_57', 'l10n_br_base.res_bank_57'),
    ('l10n_br_data_base.res_bank_58', 'l10n_br_base.res_bank_58'),
    ('l10n_br_data_base.res_bank_59', 'l10n_br_base.res_bank_59'),
    ('l10n_br_data_base.res_bank_60', 'l10n_br_base.res_bank_60'),
    ('l10n_br_data_base.res_bank_61', 'l10n_br_base.res_bank_61'),
    ('l10n_br_data_base.res_bank_62', 'l10n_br_base.res_bank_62'),
    ('l10n_br_data_base.res_bank_63', 'l10n_br_base.res_bank_63'),
    ('l10n_br_data_base.res_bank_64', 'l10n_br_base.res_bank_64'),
    ('l10n_br_data_base.res_bank_65', 'l10n_br_base.res_bank_65'),
    ('l10n_br_data_base.res_bank_66', 'l10n_br_base.res_bank_66'),
    ('l10n_br_data_base.res_bank_67', 'l10n_br_base.res_bank_67'),
    ('l10n_br_data_base.res_bank_68', 'l10n_br_base.res_bank_68'),
    ('l10n_br_data_base.res_bank_69', 'l10n_br_base.res_bank_69'),
    ('l10n_br_data_base.res_bank_70', 'l10n_br_base.res_bank_70'),
    ('l10n_br_data_base.res_bank_71', 'l10n_br_base.res_bank_71'),
    ('l10n_br_data_base.res_bank_72', 'l10n_br_base.res_bank_72'),
    ('l10n_br_data_base.res_bank_73', 'l10n_br_base.res_bank_73'),
    ('l10n_br_data_base.res_bank_74', 'l10n_br_base.res_bank_74'),
    ('l10n_br_data_base.res_bank_75', 'l10n_br_base.res_bank_75'),
    ('l10n_br_data_base.res_bank_76', 'l10n_br_base.res_bank_76'),
    ('l10n_br_data_base.res_bank_77', 'l10n_br_base.res_bank_77'),
    ('l10n_br_data_base.res_bank_78', 'l10n_br_base.res_bank_78'),
    ('l10n_br_data_base.res_bank_79', 'l10n_br_base.res_bank_79'),
    ('l10n_br_data_base.res_bank_80', 'l10n_br_base.res_bank_80'),
    ('l10n_br_data_base.res_bank_81', 'l10n_br_base.res_bank_81'),
    ('l10n_br_data_base.res_bank_82', 'l10n_br_base.res_bank_82'),
    ('l10n_br_data_base.res_bank_83', 'l10n_br_base.res_bank_83'),
    ('l10n_br_data_base.res_bank_84', 'l10n_br_base.res_bank_84'),
    ('l10n_br_data_base.res_bank_85', 'l10n_br_base.res_bank_85'),
    ('l10n_br_data_base.res_bank_86', 'l10n_br_base.res_bank_86'),
    ('l10n_br_data_base.res_bank_87', 'l10n_br_base.res_bank_87'),
    ('l10n_br_data_base.res_bank_88', 'l10n_br_base.res_bank_88'),
    ('l10n_br_data_base.res_bank_89', 'l10n_br_base.res_bank_89'),
    ('l10n_br_data_base.res_bank_90', 'l10n_br_base.res_bank_90'),
    ('l10n_br_data_base.res_bank_91', 'l10n_br_base.res_bank_91'),
    ('l10n_br_data_base.res_bank_92', 'l10n_br_base.res_bank_92'),
    ('l10n_br_data_base.res_bank_93', 'l10n_br_base.res_bank_93'),
    ('l10n_br_data_base.res_bank_94', 'l10n_br_base.res_bank_94'),
    ('l10n_br_data_base.res_bank_95', 'l10n_br_base.res_bank_95'),
    ('l10n_br_data_base.res_bank_96', 'l10n_br_base.res_bank_96'),
    ('l10n_br_data_base.res_bank_97', 'l10n_br_base.res_bank_97'),
    ('l10n_br_data_base.res_bank_98', 'l10n_br_base.res_bank_98'),
    ('l10n_br_data_base.res_bank_99', 'l10n_br_base.res_bank_99'),
    ('l10n_br_data_base.res_bank_100', 'l10n_br_base.res_bank_100'),
    ('l10n_br_data_base.res_bank_101', 'l10n_br_base.res_bank_101'),
    ('l10n_br_data_base.res_bank_102', 'l10n_br_base.res_bank_102'),
    ('l10n_br_data_base.res_bank_103', 'l10n_br_base.res_bank_103'),
    ('l10n_br_data_base.res_bank_104', 'l10n_br_base.res_bank_104'),
    ('l10n_br_data_base.res_bank_105', 'l10n_br_base.res_bank_105'),
    ('l10n_br_data_base.res_bank_106', 'l10n_br_base.res_bank_106'),
    ('l10n_br_data_base.res_bank_107', 'l10n_br_base.res_bank_107'),
    ('l10n_br_data_base.res_bank_108', 'l10n_br_base.res_bank_108'),
    ('l10n_br_data_base.res_bank_109', 'l10n_br_base.res_bank_109'),
    ('l10n_br_data_base.res_bank_110', 'l10n_br_base.res_bank_110'),
    ('l10n_br_data_base.res_bank_111', 'l10n_br_base.res_bank_111'),
    ('l10n_br_data_base.res_bank_112', 'l10n_br_base.res_bank_112'),
    ('l10n_br_data_base.res_bank_113', 'l10n_br_base.res_bank_113'),
    ('l10n_br_data_base.res_bank_114', 'l10n_br_base.res_bank_114'),
    ('l10n_br_data_base.res_bank_115', 'l10n_br_base.res_bank_115'),
    ('l10n_br_data_base.res_bank_116', 'l10n_br_base.res_bank_116'),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
