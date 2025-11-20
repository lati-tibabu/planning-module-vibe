# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MainCategory(models.Model):
    _name = 'planning.main_category'
    _description = 'Main Category'
    _order = 'sequence, id'

    name = fields.Char(string='Category Name', required=True)
    code = fields.Char(string='Category Code')
    sequence = fields.Integer(string='Sequence', default=10)
    annual_plan_id = fields.Many2one('planning.annual_plan', string='Annual Plan', required=True, ondelete='cascade')
    sub_activity_ids = fields.One2many('planning.sub_activity', 'main_category_id', string='Sub-Activities')
    description = fields.Text(string='Description')
    
    # Auto-summed monthly data
    jan_plan = fields.Float(string='Jan Plan', compute='_compute_monthly_totals', store=True)
    feb_plan = fields.Float(string='Feb Plan', compute='_compute_monthly_totals', store=True)
    mar_plan = fields.Float(string='Mar Plan', compute='_compute_monthly_totals', store=True)
    apr_plan = fields.Float(string='Apr Plan', compute='_compute_monthly_totals', store=True)
    may_plan = fields.Float(string='May Plan', compute='_compute_monthly_totals', store=True)
    jun_plan = fields.Float(string='Jun Plan', compute='_compute_monthly_totals', store=True)
    jul_plan = fields.Float(string='Jul Plan', compute='_compute_monthly_totals', store=True)
    aug_plan = fields.Float(string='Aug Plan', compute='_compute_monthly_totals', store=True)
    sep_plan = fields.Float(string='Sep Plan', compute='_compute_monthly_totals', store=True)
    oct_plan = fields.Float(string='Oct Plan', compute='_compute_monthly_totals', store=True)
    nov_plan = fields.Float(string='Nov Plan', compute='_compute_monthly_totals', store=True)
    dec_plan = fields.Float(string='Dec Plan', compute='_compute_monthly_totals', store=True)
    
    # Auto-summed quarterly data
    q1_plan = fields.Float(string='Q1 Plan', compute='_compute_quarterly_totals', store=True)
    q2_plan = fields.Float(string='Q2 Plan', compute='_compute_quarterly_totals', store=True)
    q3_plan = fields.Float(string='Q3 Plan', compute='_compute_quarterly_totals', store=True)
    q4_plan = fields.Float(string='Q4 Plan', compute='_compute_quarterly_totals', store=True)
    
    # Total
    total_plan = fields.Float(string='Total Plan', compute='_compute_total', store=True)
    
    @api.depends('sub_activity_ids.jan_plan', 'sub_activity_ids.feb_plan', 'sub_activity_ids.mar_plan',
                 'sub_activity_ids.apr_plan', 'sub_activity_ids.may_plan', 'sub_activity_ids.jun_plan',
                 'sub_activity_ids.jul_plan', 'sub_activity_ids.aug_plan', 'sub_activity_ids.sep_plan',
                 'sub_activity_ids.oct_plan', 'sub_activity_ids.nov_plan', 'sub_activity_ids.dec_plan')
    def _compute_monthly_totals(self):
        for record in self:
            record.jan_plan = sum(record.sub_activity_ids.mapped('jan_plan'))
            record.feb_plan = sum(record.sub_activity_ids.mapped('feb_plan'))
            record.mar_plan = sum(record.sub_activity_ids.mapped('mar_plan'))
            record.apr_plan = sum(record.sub_activity_ids.mapped('apr_plan'))
            record.may_plan = sum(record.sub_activity_ids.mapped('may_plan'))
            record.jun_plan = sum(record.sub_activity_ids.mapped('jun_plan'))
            record.jul_plan = sum(record.sub_activity_ids.mapped('jul_plan'))
            record.aug_plan = sum(record.sub_activity_ids.mapped('aug_plan'))
            record.sep_plan = sum(record.sub_activity_ids.mapped('sep_plan'))
            record.oct_plan = sum(record.sub_activity_ids.mapped('oct_plan'))
            record.nov_plan = sum(record.sub_activity_ids.mapped('nov_plan'))
            record.dec_plan = sum(record.sub_activity_ids.mapped('dec_plan'))
    
    @api.depends('jan_plan', 'feb_plan', 'mar_plan', 'apr_plan', 'may_plan', 'jun_plan',
                 'jul_plan', 'aug_plan', 'sep_plan', 'oct_plan', 'nov_plan', 'dec_plan')
    def _compute_quarterly_totals(self):
        for record in self:
            record.q1_plan = record.jan_plan + record.feb_plan + record.mar_plan
            record.q2_plan = record.apr_plan + record.may_plan + record.jun_plan
            record.q3_plan = record.jul_plan + record.aug_plan + record.sep_plan
            record.q4_plan = record.oct_plan + record.nov_plan + record.dec_plan
    
    @api.depends('q1_plan', 'q2_plan', 'q3_plan', 'q4_plan')
    def _compute_total(self):
        for record in self:
            record.total_plan = record.q1_plan + record.q2_plan + record.q3_plan + record.q4_plan
    
    def name_get(self):
        result = []
        for record in self:
            if record.code:
                name = f"[{record.code}] {record.name}"
            else:
                name = record.name
            result.append((record.id, name))
        return result
