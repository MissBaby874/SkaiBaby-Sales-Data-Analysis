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
```

3. Run the analysis script:

```bash
python scripts/analyze_sales.py
```

4. Open the `output/` folder to view the generated charts and summary report.
- `monthly_income.png` ✅
- `service_breakdown.png` ✅
- `summary_report.txt` ✅


## Requirements
- Python 3
- pandas
- matplotlib
- seaborn

---

## Outputs
The script generates the following files in the `output/` folder:
- monthly_income.png ✅
- service_breakdown.png ✅
- summary_report.txt ✅
These files can be viewed directly on GitHub or downloaded.

## Visualizations

### Monthly Income
![Monthly Income](output/monthly_income.png)

### Revenue Breakdown by Service
![Service Breakdown](output/service_breakdown.png)

## Summary
This project provides insights into SkaiBaby’s sales performance across different services.  
The generated charts and summary report make it easy to:
- Track monthly income trends
- Compare revenue between services
- Make informed business decisions based on data

The analysis focuses on Fatcakes, Printing & Internet, Chess Lessons, and House Calls, helping SkaiBaby optimize operations and improve profitability.

## License
MIT License
