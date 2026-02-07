# Grouping Data 
# groupby in pandas
    # Operations
        # Iterate over groups
        # Apply aggregation


grouped=df.groupby("column_name")

for name,group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()

# Aggregation  - Use groupby with multiple aggregation method like mean, max,min
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg{"numeric_column":["mean","max","min"]}

pivot=df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean"
)

# Custom aggregation
def range_func(x):
    return x.max() - x.min()

df.groupby("category_column") ["numeric_column"].agg(range_func)