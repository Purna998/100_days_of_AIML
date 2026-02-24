# Applying Linear Regression
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import numpy as np

# # Load Dataset
df=pd.read_csv("tips.csv")

# Define the variables
X=df['total_bill'].values.reshape(-1,1)
y=df['tip'].values

# Fit Linear Regression 
model=LinearRegression()
model.fit(X,y)

# Output coefficients
print("Slope: ",model.coef_[0])
print("Intercept: ",model.intercept_)
print("R-Squared: ",model.score(X,y))

# Plot Regression
sns.scatterplot(x=df['total_bill'],y=df['tip'],color='blue')
plt.plot(df['total_bill'],model.predict(X),color="red",label="Regression Line")
plt.title("Total Bill vs Tip")
plt.legend()
plt.show()