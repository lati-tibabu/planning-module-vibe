# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class WeeklyReport(models.Model):
    _name = 'planning.weekly_report'
    _description = 'Weekly Report - Gabaasa Torbee'
    _order = 'week_number desc, year desc, id desc'

    name = fields.Char(string='Report Name', compute='_compute_name', store=True)
    year = fields.Integer(string='Bara (Year)', required=True, default=lambda self: datetime.now().year)
    week_number = fields.Integer(string='Lakkoofsa Torbee (Week Number)', required=True)
    week_start_date = fields.Date(string='Guyyaa Jalqabaa (Start Date)', required=True)
    week_end_date = fields.Date(string='Guyyaa Xumuraa (End Date)', required=True)
    
    # Link to Annual Plan
    annual_plan_id = fields.Many2one('planning.annual_plan', string='Karoora Waggaa (Annual Plan)', required=True)
    main_category_id = fields.Many2one('planning.main_category', string='Ramaddii Guddaa (Main Category)', required=True)
    sub_activity_id = fields.Many2one('planning.sub_activity', string='Sochii Xiqqaa (Sub-Activity)', required=True)
    
    # Weekly data with Oromo labels
    hojii_torbee = fields.Float(string='Hojii Torbee (Weekly Plan)', help='Karoora torbee kanaaf')
    hanga_torbee = fields.Float(string='Hanga Torbee (Weekly Actual)', help='Raawwii dhugaa torbee kanaaf')
    
    # Performance calculation
    percentage_achieved = fields.Float(string='Dhibbeentaa Raawwii (% Achieved)', 
                                       compute='_compute_performance', store=True)
    cumulative_plan = fields.Float(string='Karoora Walitti Qabamiinsa (Cumulative Plan)')
    cumulative_actual = fields.Float(string='Raawwii Walitti Qabamiinsa (Cumulative Actual)')
    cumulative_percentage = fields.Float(string='Dhibbeentaa Walitti Qabamiinsa (Cumulative %)', 
                                        compute='_compute_cumulative_performance', store=True)
    
    # Status
    status = fields.Selection([
        ('on_track', 'Karaa Irratti (On Track)'),
        ('at_risk', 'Balaa Keessa (At Risk)'),
        ('off_track', 'Karaa Irraa Bahee (Off Track)')
    ], string='Haala (Status)', compute='_compute_status', store=True)
    
    notes = fields.Text(string='Yaadannoo (Notes)')
    
    @api.depends('year', 'week_number')
    def _compute_name(self):
        for record in self:
            record.name = f"Torbee {record.week_number} - {record.year}"
    
    @api.depends('hojii_torbee', 'hanga_torbee')
    def _compute_performance(self):
        for record in self:
            if record.hojii_torbee > 0:
                record.percentage_achieved = (record.hanga_torbee / record.hojii_torbee) * 100
            else:
                record.percentage_achieved = 0.0
    
    @api.depends('cumulative_plan', 'cumulative_actual')
    def _compute_cumulative_performance(self):
        for record in self:
            if record.cumulative_plan > 0:
                record.cumulative_percentage = (record.cumulative_actual / record.cumulative_plan) * 100
            else:
                record.cumulative_percentage = 0.0
    
    @api.depends('cumulative_percentage')
    def _compute_status(self):
        for record in self:
            if record.cumulative_percentage >= 90:
                record.status = 'on_track'
            elif record.cumulative_percentage >= 70:
                record.status = 'at_risk'
            else:
                record.status = 'off_track'
    
    @api.onchange('week_start_date')
    def _onchange_week_start_date(self):
        if self.week_start_date:
            self.week_end_date = self.week_start_date + timedelta(days=6)
            self.week_number = self.week_start_date.isocalendar()[1]
            self.year = self.week_start_date.year
    
    @api.onchange('annual_plan_id')
    def _onchange_annual_plan_id(self):
        if self.annual_plan_id:
            return {'domain': {'main_category_id': [('annual_plan_id', '=', self.annual_plan_id.id)]}}
        return {'domain': {'main_category_id': []}}
    
    @api.onchange('main_category_id')
    def _onchange_main_category_id(self):
        if self.main_category_id:
            return {'domain': {'sub_activity_id': [('main_category_id', '=', self.main_category_id.id)]}}
        return {'domain': {'sub_activity_id': []}}
