# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Theme(models.Model):
    _name = 'planning.theme'
    _description = 'Planning Theme'
    _order = 'sequence, id'

    name = fields.Char(string='Theme Name', required=True)
    code = fields.Char(string='Theme Code')
    sequence = fields.Integer(string='Sequence', default=10)
    strategic_plan_id = fields.Many2one('planning.strategic_plan', string='Strategic Plan', required=True, ondelete='cascade')
    strategy_ids = fields.One2many('planning.strategy', 'theme_id', string='Strategies')
    description = fields.Text(string='Description')
    
    def name_get(self):
        result = []
        for record in self:
            if record.code:
                name = f"[{record.code}] {record.name}"
            else:
                name = record.name
            result.append((record.id, name))
        return result
