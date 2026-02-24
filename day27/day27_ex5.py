# Fit a multiple linear regression model with multiple independent variables
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
x1 = np.random.rand(100,1)*10
x2 = np.random.rand(100,1)*10
x3 = np.random.rand(100,1)*10
x4 = np.random.rand(100,1)*10

y = 3*x1 + 2*x2 - 1.5*x3 + 4*x4 + np.random.randn(100,1)*2

# Combine all x variables into one matrix
X=np.hstack([x1,x2,x3,x4])

# fit the model 
mlr=LinearRegression()
mlr.fit(X,y)

# Predict for a new data point(must be 2D)
predict=mlr.predict([[12,3,5,2]])
print("Prediction: ",predict)

# Print learned coefficients
print("Coefficients:", mlr.coef_)
print("Intercept:", mlr.intercept_)

