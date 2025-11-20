# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AnnualPlan(models.Model):
    _name = 'planning.annual_plan'
    _description = 'Annual Plan'
    _order = 'year desc, id desc'

    name = fields.Char(string='Plan Name', required=True)
    year = fields.Integer(string='Year', required=True)
    description = fields.Text(string='Description')
    main_category_ids = fields.One2many('planning.main_category', 'annual_plan_id', string='Main Categories')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('closed', 'Closed')
    ], string='Status', default='draft', required=True)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.name} - {record.year}"
            result.append((record.id, name))
        return result
