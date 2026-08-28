import pandas as pd
import numpy as np

data = pd.read_csv("new_york_real_estate_2026_final.csv")
print(data.columns)
print(data.head())
data = data.dropna(subset=["sqft", "listPrice"])
x = data["sqft"].to_numpy()
y = data["listPrice"].to_numpy()
print(x.shape, y.shape)
X_mean = x.mean()
X_std = x.std()
X_norm = (x - X_mean) / X_std

y_mean = y.mean()
y_std = y.std()
y_norm = (y - y_mean) / y_std

print(X_norm[:5])
print(y_norm[:5])
# Initialize
weight = 0
bias = 0
learning_rate = 0.01
epochs = 1000

n = len(X_norm)

for i in range(epochs):
    prediction = weight * X_norm + bias
    error = prediction - y_norm
    
    weight_gradient = (error * X_norm).mean()
    bias_gradient = error.mean()
    
    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient

print("Final weight:", weight)
print("Final bias:", bias)

user_input = int(input("Enter the sqft"))
sqft = np.array(user_input)
sqft_norm = (sqft - X_mean) / X_std
predicted_norm = weight * sqft_norm + bias
predicted_price = (predicted_norm * y_std) + y_mean

print(predicted_price)