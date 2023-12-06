import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('../data/school_aggregate_sentiment_rating_average_cost_median_salary.csv')

# For cost and rating
X = sm.add_constant(df['Log Average Cost'])  # adding a constant
model_cost_rating = sm.OLS(df['Average Rating'], X).fit()
print(model_cost_rating.summary())

# For salary and rating
X = sm.add_constant(df['Log Median Salary'])  # adding a constant
model_salary_rating = sm.OLS(df['Average Rating'], X).fit()
print(model_salary_rating.summary())

# do multivariate regression
df.dropna(inplace=True)
X = sm.add_constant(df[['Median Salary', 'Net Price']])
y = df['Average Rating']

# Robust linear regression model
rlm_model = sm.RLM(y, X).fit()

print(rlm_model.summary())

import statsmodels.graphics.regressionplots as smplot

fig = smplot.plot_partregress_grid(rlm_model, fig=None)
plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
x = df['Median Salary']
y = df['Net Price']
z = df['Average Rating']
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
model_fitted_y = rlm_model.predict(sm.add_constant(np.column_stack((x_surf, y_surf))))
z_surf = np.array(model_fitted_y).reshape(x_surf.shape[0], -1)

# Plotting the regression plane
ax.plot_surface(x_surf.reshape(100, 100), y_surf.reshape(100, 100), z_surf.reshape(100, 100), alpha=0.3)

plt.show()

