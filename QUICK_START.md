# Quick Start Guide

## Odoo v16 Planning Module - Getting Started

### Prerequisites
- Odoo v16 installed and running
- Access to Odoo Apps menu (admin rights)

---

## Installation

### Step 1: Install the Module
1. Copy the `planning_module` folder to your Odoo addons directory
2. Restart your Odoo server
3. Go to **Apps** menu in Odoo
4. Click **Update Apps List**
5. Search for "Planning Module"
6. Click **Install**

### Step 2: Access the Module
After installation, you'll see a new **Planning** menu in the main navigation bar.

---

## Usage Guide

### Creating a Strategic Plan

1. Navigate to: **Planning → Strategic Planning → Strategic Plans**
2. Click **Create**
3. Fill in:
   - **Plan Name**: e.g., "Five Year Strategic Plan"
   - **Start Year**: e.g., 2025
   - **End Year**: e.g., 2029
   - **Description**: Brief overview
4. Click **Save**

#### Adding Themes
1. In the Strategic Plan form, go to the **Themes** tab
2. Add a new line
3. Enter:
   - **Code**: e.g., "EDU"
   - **Name**: e.g., "Education Development"
   - **Description**: Theme details
4. Save

#### Adding Strategies
1. Click on a Theme to open its form
2. Go to the **Strategies** tab
3. Add strategies with:
   - **Code**: e.g., "EDU-INF"
   - **Name**: e.g., "Infrastructure Development"
   - **Description**: Strategy details
4. Go to **Yearly Targets** tab
5. Enter targets for each year (the years shown will match your strategic plan's range)

---

### Creating an Annual Plan

1. Navigate to: **Planning → Annual Planning → Annual Plans**
2. Click **Create**
3. Fill in:
   - **Plan Name**: e.g., "Annual Plan 2025"
   - **Year**: 2025
   - **Description**: Plan overview
4. Click **Save**

#### Adding Main Categories
1. In the Annual Plan form, go to the **Main Categories** tab
2. Add categories like:
   - "Construction Projects"
   - "Training Programs"
   - "Equipment Procurement"

#### Adding Sub-Activities
1. Click on a Main Category to open it
2. Go to the **Sub-Activities** tab
3. Add sub-activities
4. Click on a sub-activity to open its form
5. Go to the **Monthly Plan** tab
6. Enter planned values for each month (Jan-Dec)
7. The system automatically calculates:
   - Quarterly totals (Q1-Q4)
   - Annual total

#### Viewing Auto-Summed Data
1. Open a Main Category
2. Go to the **Monthly Summary** tab
3. See automatically aggregated data from all sub-activities:
   - Monthly totals (Jan-Dec)
   - Quarterly totals (Q1-Q4)
   - Annual total

#### Entering Actual Data
1. Open a Sub-Activity
2. Go to the **Monthly Actual** tab
3. Enter actual achievement for each month
4. The system calculates quarterly and annual actuals

---

### Creating Weekly Reports (Gabaasa Torbee)

1. Navigate to: **Planning → Gabaasa Torbee (Weekly Reports) → Weekly Reports**
2. Click **Create**
3. Fill in:
   - **Bara (Year)**: 2025
   - **Guyyaa Jalqabaa (Start Date)**: Select the week start date
   - The system automatically fills:
     - Week Number
     - End Date (7 days after start)
4. Select:
   - **Karoora Waggaa (Annual Plan)**
   - **Ramaddii Guddaa (Main Category)**
   - **Sochii Xiqqaa (Sub-Activity)**
5. Enter:
   - **Hojii Torbee (Weekly Plan)**: Planned target for the week
   - **Hanga Torbee (Weekly Actual)**: Actual achievement
   - **Cumulative Plan**: Total plan up to this week
   - **Cumulative Actual**: Total actual up to this week
6. The system automatically calculates:
   - **Weekly Achievement %**: (Hanga Torbee / Hojii Torbee) × 100
   - **Cumulative %**: (Cumulative Actual / Cumulative Plan) × 100
   - **Status**:
     - **Karaa Irratti (On Track)**: ≥90%
     - **Balaa Keessa (At Risk)**: 70-89%
     - **Karaa Irraa Bahee (Off Track)**: <70%
7. Add **Yaadannoo (Notes)** if needed
8. Click **Save**

---

### Using the Weekly Report Dashboard

#### Kanban View (Default)
- Shows reports as cards with color-coded status
- Green: On Track
- Yellow: At Risk
- Red: Off Track

#### Tree View
- List view with sortable columns
- Color-coded rows based on status
- Quick overview of all reports

#### Pivot View
- For data analysis and aggregation
- Group by year, category, or activity
- Summarize performance metrics

#### Graph View
- Visual representation of trends
- Compare Hojii Torbee vs Hanga Torbee
- Track performance over time

---

## Demo Data

The module includes demo data to help you understand the features:

### Sample Strategic Plan
- **Name**: Five Year Strategic Plan (2025-2029)
- **Themes**: Education Development, Health Services
- **Strategies**: Infrastructure Development, Quality Improvement, Healthcare Access

### Sample Annual Plan
- **Year**: 2025
- **Main Categories**: Construction Projects, Training Programs
- **Sub-Activities**: School Building, Health Clinic, Teacher Training

### Sample Weekly Reports
- 3 weekly reports showing different performance levels
- Demonstrates status calculation and color coding

To view demo data:
1. Install the module **with demo data enabled**
2. Navigate to the respective menus
3. Explore the pre-populated records

---

## Key Features to Remember

### Auto-Summing in Annual Plans
- Main Categories automatically aggregate data from Sub-Activities
- Updates in real-time when you change sub-activity data
- No manual calculation needed

### Dynamic Years in Strategic Plans
- Set any year range (e.g., 2025-2030, 2024-2028)
- Strategies automatically show the correct years
- Supports 1-5 year plans

### Performance Tracking
- Weekly reports automatically calculate achievement percentages
- Color-coded status helps identify issues quickly
- Cumulative tracking shows overall progress

### Oromo Language Support
- Weekly reports use Oromo labels
- Bilingual display (Oromo + English)
- Cultural relevance for Ethiopian context

---

## Tips and Best Practices

1. **Start with Strategic Planning**: Define your long-term goals first
2. **Link Annual Plans to Strategy**: Ensure alignment with strategic objectives
3. **Regular Updates**: Update Weekly Reports consistently for accurate tracking
4. **Use Cumulative Data**: Track overall progress, not just weekly performance
5. **Review Status Colors**: Pay attention to "At Risk" and "Off Track" items
6. **Add Notes**: Use the Yaadannoo field to document important context
7. **Analyze Trends**: Use Pivot and Graph views to identify patterns

---

## Troubleshooting

### Module Not Appearing After Installation
- Make sure you updated the apps list
- Check if the module is in the correct addons directory
- Restart the Odoo server

### Auto-Sum Not Working
- Ensure sub-activities are saved
- Check that they're linked to the correct main category
- Refresh the page

### Dates in Weekly Report
- Select the Start Date first
- The system will auto-fill Week Number and End Date
- You can manually adjust if needed

---

## Support and Documentation

For more detailed information, see:
- **Module Documentation**: `planning_module/README.md`
- **Architecture Overview**: `ARCHITECTURE.md`
- **Implementation Details**: `IMPLEMENTATION_SUMMARY.md`

---

## Version Information

- **Module Version**: 16.0.1.0.0
- **Odoo Version**: 16.0
- **License**: LGPL-3

---

## Next Steps

1. Install the module
2. Review the demo data
3. Create your first Strategic Plan
4. Set up your Annual Plan
5. Start tracking with Weekly Reports

**Happy Planning!** 🎯
