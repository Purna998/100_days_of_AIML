# Combining and Merging DataFrames
# - Concatenation
# - Merging
# - Joining

#concatenation
combined = pd.concat([df1,df2],axis=0)
combined = pd.concat([df1,df2],axis=1)

#Merging
merged=pd.merge(df1,df2,on="Common_column")
merged=pd.merge(df1,df2,how="left",on="common_column")
merged=pd.merge(df1,df2,how="inner",on="common_column")

#Joining
joined=df1.join(df2,how="inner")