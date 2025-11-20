# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StrategicPlan(models.Model):
    _name = 'planning.strategic_plan'
    _description = 'Strategic Plan'
    _order = 'start_year desc, id desc'

    name = fields.Char(string='Plan Name', required=True)
    start_year = fields.Integer(string='Start Year', required=True)
    end_year = fields.Integer(string='End Year', required=True)
    description = fields.Text(string='Description')
    theme_ids = fields.One2many('planning.theme', 'strategic_plan_id', string='Themes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('closed', 'Closed')
    ], string='Status', default='draft', required=True)
    
    @api.constrains('start_year', 'end_year')
    def _check_years(self):
        for record in self:
            if record.end_year < record.start_year:
                raise models.ValidationError('End year must be greater than or equal to start year.')
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.name} ({record.start_year}-{record.end_year})"
            result.append((record.id, name))
        return result
