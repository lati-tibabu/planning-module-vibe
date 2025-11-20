# Planning Module for Odoo v16

## Overview

This module provides comprehensive planning functionality for Odoo v16, including:
- Strategic Planning with dynamic yearly ranges
- Annual Planning with hierarchical structure
- Weekly Reporting with Plan vs Actual tracking

## Features

### 1. Strategic Plan
- Define strategic plans with dynamic yearly ranges (start year to end year)
- Organize plans using Themes and Strategies
- Set yearly targets for each strategy
- Track plan status (Draft, Active, Closed)

### 2. Annual Plan
- Create annual plans for specific years
- Hierarchical structure with Main Categories and Sub-Activities
- Main Categories automatically sum monthly/quarterly data from sub-activities
- Support for both Plan and Actual data entry

### 3. Weekly Report (Gabaasa Torbee)
- Operational dashboard for tracking weekly performance
- Plan vs. Actual comparison with percentage calculations
- Cumulative performance tracking
- Status indicators (On Track, At Risk, Off Track)
- Specific Oromo language labels for Ethiopian context

## Installation

1. Copy the `planning_module` directory to your Odoo addons path
2. Update the addons list in Odoo
3. Install the module from Apps menu

## Usage

### Strategic Planning
1. Navigate to Planning > Strategic Planning > Strategic Plans
2. Create a new strategic plan with start and end years
3. Add themes to the strategic plan
4. Define strategies under each theme
5. Set yearly targets for each strategy

### Annual Planning
1. Navigate to Planning > Annual Planning > Annual Plans
2. Create an annual plan for a specific year
3. Add main categories to the plan
4. Create sub-activities under each main category
5. Enter monthly plan data for each sub-activity
6. Main categories will automatically sum the values from sub-activities

### Weekly Reporting
1. Navigate to Planning > Gabaasa Torbee (Weekly Reports)
2. Create a new weekly report
3. Select the annual plan, main category, and sub-activity
4. Enter weekly plan (Hojii Torbee) and actual (Hanga Torbee) values
5. System automatically calculates performance percentages
6. Track cumulative performance over time

## Oromo Language Labels

The Weekly Report uses specific Oromo language labels:
- **Hojii Torbee**: Weekly Plan
- **Hanga Torbee**: Weekly Actual
- **Gabaasa Torbee**: Weekly Report
- **Bara**: Year
- **Lakkoofsa Torbee**: Week Number
- **Guyyaa Jalqabaa**: Start Date
- **Guyyaa Xumuraa**: End Date
- **Karoora Waggaa**: Annual Plan
- **Ramaddii Guddaa**: Main Category
- **Sochii Xiqqaa**: Sub-Activity
- **Dhibbeentaa Raawwii**: Percentage Achieved
- **Walitti Qabamiinsa**: Cumulative
- **Haala**: Status
- **Yaadannoo**: Notes

## Technical Details

### Models
- `planning.strategic_plan`: Strategic plan management
- `planning.theme`: Themes under strategic plans
- `planning.strategy`: Strategies under themes with yearly targets
- `planning.annual_plan`: Annual plan management
- `planning.main_category`: Main categories with auto-sum functionality
- `planning.sub_activity`: Sub-activities with monthly plan and actual data
- `planning.weekly_report`: Weekly performance tracking

### Key Features
- **Auto-summing**: Main categories automatically aggregate data from sub-activities
- **Computed Fields**: Quarterly and total values are automatically calculated
- **Dynamic Years**: Strategic plans support flexible year ranges
- **Performance Tracking**: Automatic calculation of achievement percentages
- **Status Indicators**: Visual status based on performance thresholds

## License

LGPL-3

## Author

Planning Team
