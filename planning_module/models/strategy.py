# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Strategy(models.Model):
    _name = 'planning.strategy'
    _description = 'Planning Strategy'
    _order = 'sequence, id'

    name = fields.Char(string='Strategy Name', required=True)
    code = fields.Char(string='Strategy Code')
    sequence = fields.Integer(string='Sequence', default=10)
    theme_id = fields.Many2one('planning.theme', string='Theme', required=True, ondelete='cascade')
    strategic_plan_id = fields.Many2one('planning.strategic_plan', related='theme_id.strategic_plan_id', 
                                        string='Strategic Plan', store=True, readonly=True)
    description = fields.Text(string='Description')
    
    # Dynamic yearly targets
    target_year_1 = fields.Float(string='Year 1 Target')
    target_year_2 = fields.Float(string='Year 2 Target')
    target_year_3 = fields.Float(string='Year 3 Target')
    target_year_4 = fields.Float(string='Year 4 Target')
    target_year_5 = fields.Float(string='Year 5 Target')
    
    @api.depends('theme_id')
    def _compute_display_years(self):
        for record in self:
            if record.strategic_plan_id:
                record.display_year_1 = str(record.strategic_plan_id.start_year)
                years_diff = record.strategic_plan_id.end_year - record.strategic_plan_id.start_year
                for i in range(2, 6):
                    if i - 1 <= years_diff:
                        setattr(record, f'display_year_{i}', str(record.strategic_plan_id.start_year + i - 1))
                    else:
                        setattr(record, f'display_year_{i}', '')
    
    display_year_1 = fields.Char(string='Year 1', compute='_compute_display_years')
    display_year_2 = fields.Char(string='Year 2', compute='_compute_display_years')
    display_year_3 = fields.Char(string='Year 3', compute='_compute_display_years')
    display_year_4 = fields.Char(string='Year 4', compute='_compute_display_years')
    display_year_5 = fields.Char(string='Year 5', compute='_compute_display_years')
    
    def name_get(self):
        result = []
        for record in self:
            if record.code:
                name = f"[{record.code}] {record.name}"
            else:
                name = record.name
            result.append((record.id, name))
        return result
