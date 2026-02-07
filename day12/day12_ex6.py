# Use Pivot_table to calculate total sales per region and per year
import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create pivot table
pivot_table = pd.pivot_table(
    df,
    values="Sales_Amount",
    index="Region",
    columns="Year",
    aggfunc="sum"
)

print("Total Sales per Region per Year:\n")
print(pivot_table)
