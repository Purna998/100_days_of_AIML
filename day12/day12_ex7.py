# Create a custom aggregation function to calculate the variance for each group
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Region": ["East", "East", "West", "West", "North", "North"],
    "Sales_Amount": [10000, 12000, 15000, 14000, 9000, 11000]
})

# Custom aggregation function of variance
def custom_variance(series):
    return np.var(series, ddof=1) # ddof=1 - sample variance 
