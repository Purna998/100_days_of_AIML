# calculating summary statistics for Grouped Data
# Common Statistics: Mean, Max, Min

df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

# Single Aggregation
df.groupby("category_column")["numeric_column"].mean()

# Multi-Aggregation
df.groupby("category_column").agg(
    {"numeric_column":["mean","max","min"]}
)