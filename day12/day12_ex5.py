# Create a dataset of sales data and group it by region or product category
import pandas as pd

# Load the sales dataset
df=pd.read_csv("sales_data.csv")
# print(df.head())

# Taking just four columns
new_df=df.loc[:,["Sales_Rep","Product_Category","Region","Sales_Amount"]]
print("Original Dataset: \n",new_df)

region_grouped=new_df.groupby("Region")["Sales_Amount"].mean()
print("\nAfter grouping Sales amount with region:\n",region_grouped)

category_grouped=new_df.groupby("Product_Category")["Sales_Amount"].mean()
print("\nAfter grouping Sales amount with Product Category:\n",category_grouped)