import numpy as np
import matplotlib.pyplot as plt

def locally_weighted_regression(x, X, y, tau):
    weights = np.exp(-((X - x)**2) / (2 * tau**2))  
    weighted_sum = np.sum(weights * y)             
    weight_total = np.sum(weights)                 
    return weighted_sum / weight_total             

np.random.seed(42)
X = np.linspace(1, 10, 100)                        
y = 2 * X + np.random.normal(0, 2, X.shape)        

tau = 1.0

predictions = [locally_weighted_regression(x, X, y, tau) for x in X]

plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Data Points", color="blue", alpha=0.6)
plt.plot(X, predictions, label="LWR Curve (tau=1.0)", color="red", linewidth=2)
plt.title("Locally Weighted Regression (Simplified)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
