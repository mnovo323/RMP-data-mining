import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

aggregate_sentiment = pd.read_csv('../data/school_aggregate_sentiment_rating_average_cost_median_salary.csv')

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
x = aggregate_sentiment['Median Salary']
y = aggregate_sentiment['Net Price']
z = aggregate_sentiment['Average Rating']
ax.scatter(x, y, z, color='b', marker='o')

# Labels and Title
ax.set_xlabel('Median Salary')
ax.set_ylabel('Net Price')
ax.set_zlabel('Average Rating')
ax.set_title('3D Scatter Plot with Regression Plane')

# Create grid coordinates for plotting
x_surf, y_surf = np.meshgrid(np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100))
x_surf = x_surf.flatten()
y_surf = y_surf.flatten()

# Predict values
model_fitted_y = model.predict(sm.add_constant(np.column_stack((x_surf, y_surf))))
z_surf = np.array(model_fitted_y).reshape(x_surf.shape[0], -1)

# Plotting the regression plane
ax.plot_surface(x_surf.reshape(100, 100), y_surf.reshape(100, 100), z_surf.reshape(100, 100), alpha=0.3)

plt.show()
