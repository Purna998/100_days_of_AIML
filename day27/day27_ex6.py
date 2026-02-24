# Compare correlation and regression results for non-linear relationships
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

# Generate non-linear data
np.random.seed(42)
x = np.random.rand(100,1)*10
y = 3*(x**2) + np.random.randn(100,1)*5

# Create DataFrame
data = pd.DataFrame(np.hstack([x,y]), columns=["x","y"])

# 1. Correlation
correlation_matrix = data.corr()
print("Correlation Matrix:\n", correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 2. Linear Regression
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

print("Linear Regression Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("R² Score (Linear Model):", r2_score(y, y_pred))

# 3. Visualization
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_pred, color="red", label="Linear Fit")
plt.title("Linear Regression on Non-Linear Data")
plt.legend()
plt.show()