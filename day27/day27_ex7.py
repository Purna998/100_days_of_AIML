# Use real-world datasets (e.g housing prices) for regression analysis
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("HousePricePrediction.xlsx")

# Separate features and target
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

# Convert categorical features
X = pd.get_dummies(X, drop_first=True)

# Fill missing values with mean
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
y=y.fillna(y.mean())

# Train Linear Regression
model = LinearRegression()
model.fit(X, y)

print("R² Score:", model.score(X, y))

# Optional: Actual vs Predicted
y_pred = model.predict(X)
plt.scatter(y, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()