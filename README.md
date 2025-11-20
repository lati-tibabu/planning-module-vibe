# planning-module-vibe

## Odoo v16 Planning Module

This repository contains a comprehensive planning module for Odoo v16, designed to support strategic planning, annual planning, and weekly operational reporting.

## Features

### Strategic Plan
- Dynamic yearly ranges for strategic planning
- Themes and Strategies organization
- Flexible target setting for multiple years

### Annual Plan
- Hierarchical planning structure
- Main Categories with automatic aggregation
- Sub-Activities with monthly and quarterly breakdowns
- Plan vs. Actual tracking

### Weekly Report (Gabaasa Torbee)
- Operational dashboard with specific Oromo language labels
- Plan vs. Actual performance tracking
- Cumulative percentage calculations
- Status indicators based on performance

## Installation

1. Clone this repository to your Odoo addons directory
2. Install the module through Odoo Apps menu

## Documentation

See the [Planning Module README](planning_module/README.md) for detailed documentation.

## Module Structure

```
planning_module/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── strategic_plan.py
│   ├── theme.py
│   ├── strategy.py
│   ├── annual_plan.py
│   ├── main_category.py
│   ├── sub_activity.py
│   └── weekly_report.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── strategic_plan_views.xml
    ├── annual_plan_views.xml
    ├── weekly_report_views.xml
    └── menu_views.xml
```

## License

LGPL-3