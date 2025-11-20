# Module Architecture Overview

## Data Flow and Relationships

```
Strategic Planning Layer (Long-term)
=====================================
┌─────────────────────────────────────────────────────────────┐
│  Strategic Plan (2025-2029)                                 │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Theme 1: Education Development                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Strategy 1: Infrastructure Development         │  │  │
│  │  │    Targets: Y1=100, Y2=150, Y3=200, Y4=250, ... │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Strategy 2: Quality Improvement                │  │  │
│  │  │    Targets: Y1=80, Y2=85, Y3=90, ...            │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Theme 2: Health Services                            │  │
│  │  └── Strategy 3: Healthcare Access                   │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

Annual Planning Layer (Mid-term)
=================================
┌─────────────────────────────────────────────────────────────┐
│  Annual Plan 2025                                           │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Main Category 1: Construction Projects              │  │
│  │  (Auto-summed from sub-activities)                    │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Sub-Activity 1: School Building                │  │  │
│  │  │    Jan=5, Feb=5, Mar=8, ..., Total=110          │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │  Sub-Activity 2: Clinic Building                │  │  │
│  │  │    Jan=3, Feb=3, Mar=5, ..., Total=74           │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  │  TOTAL: Q1=auto, Q2=auto, Q3=auto, Q4=auto          │  │  │
│  └───────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Main Category 2: Training Programs                  │  │
│  │  └── Sub-Activity 3: Teacher Training                │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

Weekly Reporting Layer (Operational)
=====================================
┌─────────────────────────────────────────────────────────────┐
│  Gabaasa Torbee (Weekly Report)                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Week 1 - School Building                            │  │
│  │    Hojii Torbee (Plan):    1.5                       │  │
│  │    Hanga Torbee (Actual):  1.3                       │  │
│  │    Weekly %:               86.7%                      │  │
│  │    Cumulative %:           86.7%                      │  │
│  │    Status: At Risk (Balaa Keessa)                    │  │
│  └───────────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Week 2 - School Building                            │  │
│  │    Hojii Torbee (Plan):    1.2                       │  │
│  │    Hanga Torbee (Actual):  1.4                       │  │
│  │    Weekly %:               116.7%                     │  │
│  │    Cumulative %:           100%                       │  │
│  │    Status: On Track (Karaa Irratti)                  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Key Computed Fields and Auto-calculations

### Main Category (Auto-Sum from Sub-Activities)
```python
Monthly Totals:
  jan_plan = SUM(all sub_activity.jan_plan)
  feb_plan = SUM(all sub_activity.feb_plan)
  ... for all 12 months

Quarterly Totals:
  q1_plan = jan_plan + feb_plan + mar_plan
  q2_plan = apr_plan + may_plan + jun_plan
  q3_plan = jul_plan + aug_plan + sep_plan
  q4_plan = oct_plan + nov_plan + dec_plan

Annual Total:
  total_plan = q1_plan + q2_plan + q3_plan + q4_plan
```

### Weekly Report (Performance Calculations)
```python
Weekly Achievement:
  percentage_achieved = (hanga_torbee / hojii_torbee) × 100

Cumulative Achievement:
  cumulative_percentage = (cumulative_actual / cumulative_plan) × 100

Status Determination:
  if cumulative_percentage >= 90%  → On Track
  if cumulative_percentage >= 70%  → At Risk
  if cumulative_percentage < 70%   → Off Track
```

## Oromo Language Labels in Weekly Report

| Oromo Label          | English Translation  | Field/Purpose                |
|---------------------|----------------------|------------------------------|
| Gabaasa Torbee      | Weekly Report        | Model name                   |
| Hojii Torbee        | Weekly Plan          | Weekly planned target        |
| Hanga Torbee        | Weekly Actual        | Weekly actual achievement    |
| Bara                | Year                 | Report year                  |
| Lakkoofsa Torbee    | Week Number          | Week number in year          |
| Guyyaa Jalqabaa     | Start Date           | Week start date              |
| Guyyaa Xumuraa      | End Date             | Week end date                |
| Karoora Waggaa      | Annual Plan          | Link to annual plan          |
| Ramaddii Guddaa     | Main Category        | Link to main category        |
| Sochii Xiqqaa       | Sub-Activity         | Link to sub-activity         |
| Dhibbeentaa Raawwii | % Achieved           | Performance percentage       |
| Walitti Qabamiinsa  | Cumulative           | Cumulative totals            |
| Haala               | Status               | Performance status           |
| Karaa Irratti       | On Track             | Status: ≥90%                 |
| Balaa Keessa        | At Risk              | Status: ≥70%                 |
| Karaa Irraa Bahee   | Off Track            | Status: <70%                 |
| Yaadannoo           | Notes                | Additional notes             |

## User Workflows

### 1. Strategic Planning Workflow
```
1. Create Strategic Plan (e.g., 2025-2029)
2. Add Themes (e.g., Education, Health)
3. Define Strategies under each Theme
4. Set yearly targets for each Strategy (Year 1-5)
```

### 2. Annual Planning Workflow
```
1. Create Annual Plan for specific year (e.g., 2025)
2. Add Main Categories
3. Create Sub-Activities under each Main Category
4. Enter monthly Plan data for each Sub-Activity
5. Main Category automatically shows aggregated totals
6. Enter monthly Actual data as work progresses
```

### 3. Weekly Reporting Workflow
```
1. Create Weekly Report
2. Select Annual Plan, Main Category, and Sub-Activity
3. Enter Hojii Torbee (Weekly Plan)
4. Enter Hanga Torbee (Weekly Actual)
5. System automatically calculates:
   - Weekly achievement percentage
   - Cumulative plan and actual
   - Cumulative percentage
   - Status indicator
6. Review dashboard with color-coded status
```

## View Types Available

### Strategic Plan
- Tree View: List all strategic plans
- Form View: Edit plan, themes, and strategies

### Annual Plan
- Tree View: List all annual plans
- Form View: Edit plan with main categories
- Main Category Form: Shows auto-summed monthly/quarterly data
- Sub-Activity Form: Enter monthly plan and actual data

### Weekly Report
- Kanban View: Dashboard cards with status colors
- Tree View: Sortable list with color coding
- Form View: Data entry form
- Pivot View: Analysis and aggregation
- Graph View: Performance trends visualization

## Security

All models have access control configured for `base.group_user`:
- Read: ✓
- Write: ✓
- Create: ✓
- Unlink: ✓
