# -*- coding: utf-8 -*-
{
    'name': 'Planning Module',
    'version': '16.0.1.0.0',
    'category': 'Planning',
    'summary': 'Strategic Planning, Annual Planning, and Weekly Reporting',
    'description': """
        Planning Module for Odoo v16
        =============================
        
        Features:
        ---------
        * Strategic Plan with dynamic yearly ranges under Themes/Strategies
        * Annual Plan with hierarchical structure
        * Main Categories that auto-sum monthly/quarterly data from sub-activities
        * Weekly Report dashboard tracking Plan vs. Actual and Cumulative % performance
    """,
    'author': 'Planning Team',
    'website': 'https://github.com/lati-tibabu/planning-module-vibe',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/strategic_plan_views.xml',
        'views/annual_plan_views.xml',
        'views/weekly_report_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
