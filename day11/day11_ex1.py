df=df.dropna() # drop rows with missing values
df=df.dropna(axis=1) # drop column with missing values

# Fill 
df["column_name"]=df["column_name"].fillna(0) # fill zero in rows with missing values

df.fillna(method="ffill") # forward fill
df.fillna(method="bfill") # backward fill

df["column_name"]=df["column_name"].interpolate()
