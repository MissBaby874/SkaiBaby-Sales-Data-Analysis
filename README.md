# SkaiBaby Sales Data Analysis

## Project Overview
This is a structured Python-based sales data analysis project for **SkaiBaby**, organized into **data**, **scripts**, and **output** layers.  
The project transforms raw sales data into actionable business insights, including:

- Monthly income trends
- Revenue breakdown by service
- Visualizations for presentations
- A summary report for decision-making

---

## Folder Structure

SkaiBaby-Sales-Data-Analysis/
│
├── data/
│   └── skaibaby_sales.csv      # Raw sales data
│
├── scripts/
│   └── analyze_sales.py        # Python script to analyze data
│
├── output/
│   ├── monthly_income.png      # Monthly income chart
│   ├── service_breakdown.png   # Revenue per service chart
│   └── summary_report.txt      # Summary report
│
└── README.md                   # Project overview and instructions

---

## Example CSV Data
Below is a **sample of the sales data** used in this project:

| date       | service               | amount |
|------------|-----------------------|--------|
| 2025-01-05 | Fatcakes              | 550    |
| 2025-01-06 | Printing & Internet   | 120    |
| 2025-01-07 | Chess Lessons         | 200    |
| 2025-01-10 | House Calls           | 300    |
| 2025-02-10 | Fatcakes              | 800    |

---

## How to Run
1. Make sure **Python 3** is installed *(Pydroid 3 works on Android)*  

2. Install required packages:
```bash
pip install pandas matplotlib seaborn


## Run the Analysis Script
After installing the packages, run the Python script to generate your outputs:

```bash
python scripts/analyze_sales.py


