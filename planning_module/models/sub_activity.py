# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubActivity(models.Model):
    _name = 'planning.sub_activity'
    _description = 'Sub-Activity'
    _order = 'sequence, id'

    name = fields.Char(string='Activity Name', required=True)
    code = fields.Char(string='Activity Code')
    sequence = fields.Integer(string='Sequence', default=10)
    main_category_id = fields.Many2one('planning.main_category', string='Main Category', required=True, ondelete='cascade')
    annual_plan_id = fields.Many2one('planning.annual_plan', related='main_category_id.annual_plan_id', 
                                     string='Annual Plan', store=True, readonly=True)
    description = fields.Text(string='Description')
    
    # Monthly plan data
    jan_plan = fields.Float(string='Jan Plan', default=0.0)
    feb_plan = fields.Float(string='Feb Plan', default=0.0)
    mar_plan = fields.Float(string='Mar Plan', default=0.0)
    apr_plan = fields.Float(string='Apr Plan', default=0.0)
    may_plan = fields.Float(string='May Plan', default=0.0)
    jun_plan = fields.Float(string='Jun Plan', default=0.0)
    jul_plan = fields.Float(string='Jul Plan', default=0.0)
    aug_plan = fields.Float(string='Aug Plan', default=0.0)
    sep_plan = fields.Float(string='Sep Plan', default=0.0)
    oct_plan = fields.Float(string='Oct Plan', default=0.0)
    nov_plan = fields.Float(string='Nov Plan', default=0.0)
    dec_plan = fields.Float(string='Dec Plan', default=0.0)
    
    # Monthly actual data
    jan_actual = fields.Float(string='Jan Actual', default=0.0)
    feb_actual = fields.Float(string='Feb Actual', default=0.0)
    mar_actual = fields.Float(string='Mar Actual', default=0.0)
    apr_actual = fields.Float(string='Apr Actual', default=0.0)
    may_actual = fields.Float(string='May Actual', default=0.0)
    jun_actual = fields.Float(string='Jun Actual', default=0.0)
    jul_actual = fields.Float(string='Jul Actual', default=0.0)
    aug_actual = fields.Float(string='Aug Actual', default=0.0)
    sep_actual = fields.Float(string='Sep Actual', default=0.0)
    oct_actual = fields.Float(string='Oct Actual', default=0.0)
    nov_actual = fields.Float(string='Nov Actual', default=0.0)
    dec_actual = fields.Float(string='Dec Actual', default=0.0)
    
    # Quarterly totals
    q1_plan = fields.Float(string='Q1 Plan', compute='_compute_quarterly_totals', store=True)
    q2_plan = fields.Float(string='Q2 Plan', compute='_compute_quarterly_totals', store=True)
    q3_plan = fields.Float(string='Q3 Plan', compute='_compute_quarterly_totals', store=True)
    q4_plan = fields.Float(string='Q4 Plan', compute='_compute_quarterly_totals', store=True)
    
    q1_actual = fields.Float(string='Q1 Actual', compute='_compute_quarterly_totals', store=True)
    q2_actual = fields.Float(string='Q2 Actual', compute='_compute_quarterly_totals', store=True)
    q3_actual = fields.Float(string='Q3 Actual', compute='_compute_quarterly_totals', store=True)
    q4_actual = fields.Float(string='Q4 Actual', compute='_compute_quarterly_totals', store=True)
    
    # Totals
    total_plan = fields.Float(string='Total Plan', compute='_compute_totals', store=True)
    total_actual = fields.Float(string='Total Actual', compute='_compute_totals', store=True)
    
    @api.depends('jan_plan', 'feb_plan', 'mar_plan', 'apr_plan', 'may_plan', 'jun_plan',
                 'jul_plan', 'aug_plan', 'sep_plan', 'oct_plan', 'nov_plan', 'dec_plan',
                 'jan_actual', 'feb_actual', 'mar_actual', 'apr_actual', 'may_actual', 'jun_actual',
                 'jul_actual', 'aug_actual', 'sep_actual', 'oct_actual', 'nov_actual', 'dec_actual')
    def _compute_quarterly_totals(self):
        for record in self:
            # Plan
            record.q1_plan = record.jan_plan + record.feb_plan + record.mar_plan
            record.q2_plan = record.apr_plan + record.may_plan + record.jun_plan
            record.q3_plan = record.jul_plan + record.aug_plan + record.sep_plan
            record.q4_plan = record.oct_plan + record.nov_plan + record.dec_plan
            # Actual
            record.q1_actual = record.jan_actual + record.feb_actual + record.mar_actual
            record.q2_actual = record.apr_actual + record.may_actual + record.jun_actual
            record.q3_actual = record.jul_actual + record.aug_actual + record.sep_actual
            record.q4_actual = record.oct_actual + record.nov_actual + record.dec_actual
    
    @api.depends('q1_plan', 'q2_plan', 'q3_plan', 'q4_plan',
                 'q1_actual', 'q2_actual', 'q3_actual', 'q4_actual')
    def _compute_totals(self):
        for record in self:
            record.total_plan = record.q1_plan + record.q2_plan + record.q3_plan + record.q4_plan
            record.total_actual = record.q1_actual + record.q2_actual + record.q3_actual + record.q4_actual
    
    def name_get(self):
        result = []
        for record in self:
            if record.code:
                name = f"[{record.code}] {record.name}"
            else:
                name = record.name
            result.append((record.id, name))
        return result
