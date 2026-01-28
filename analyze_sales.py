import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------
# Paths (absolute for Android / Pydroid 3)
data_path = '/storage/emulated/0/Pydroid 3/SkaiBaby-Sales-Data-Analysis/data/skaibaby_sales.csv'
output_folder = '/storage/emulated/0/Pydroid 3/SkaiBaby-Sales-Data-Analysis/output'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ----------------------
# Load CSV data
df = pd.read_csv(data_path, parse_dates=['date'])

# ----------------------
# Monthly income
df['month'] = df['date'].dt.to_period('M')
monthly_income = df.groupby('month')['amount'].sum().reset_index()

# Plot monthly income
plt.figure(figsize=(8,5))
sns.barplot(x=monthly_income['month'].astype(str), y=monthly_income['amount'], palette='coolwarm')
plt.title('Monthly Income')
plt.ylabel('Revenue (R)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'monthly_income.png'))
plt.close()

# ----------------------
# Revenue per service
service_revenue = df.groupby('service')['amount'].sum().reset_index()

# Plot service breakdown
plt.figure(figsize=(6,4))
sns.barplot(x='service', y='amount', data=service_revenue, palette='viridis')
plt.title('Revenue by Service')
plt.ylabel('Revenue (R)')
plt.xlabel('Service')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'service_breakdown.png'))
plt.close()

# ----------------------
# Summary report
summary_path = os.path.join(output_folder, 'summary_report.txt')
with open(summary_path, 'w') as f:
    f.write('SkaiBaby Sales Summary Report\n')
    f.write('============================\n\n')
    f.write('Monthly Income:\n')
    f.write(monthly_income.to_string(index=False))
    f.write('\n\nRevenue per Service:\n')
    f.write(service_revenue.to_string(index=False))

print("Analysis complete! Check the output folder.")