import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

aggregate_sentiment = pd.read_csv('../data/school_aggregate_sentiment_rating_average_cost_median_salary.csv')

# Scatter plot for Median Salary vs Average Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Median Salary', y='Average Rating', data=aggregate_sentiment, alpha=0.5)
sns.regplot(x='Median Salary', y='Average Rating', data=aggregate_sentiment, scatter=False, color='red')
plt.title('Median Salary vs Average Rating')
plt.xlabel('Median Salary ($)')
plt.ylabel('Average Rating')
plt.show()

# Scatter plot for Net Price vs Average Rating
plt.figure(figsize=(10, 6))
aggregate_sentiment.dropna(inplace=True)
sns.scatterplot(x='Net Price', y='Average Rating', data=aggregate_sentiment, alpha=0.5)
sns.regplot(x='Net Price', y='Average Rating', data=aggregate_sentiment, scatter=False, color='red')
plt.title('Net Price vs Average Rating')
plt.xlabel('Net Price ($)')
plt.ylabel('Average Rating')
plt.show()

# Using coefficients from the regression model
net_price_coeff = -3.806e-06  # Replace with your actual coefficient
const = 2.7213  # Replace with your actual intercept

# Calculate the predicted Average Rating
aggregate_sentiment['Predicted Rating'] = const + net_price_coeff * aggregate_sentiment['Net Price']

# Scatter plot with custom regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Net Price', y='Average Rating', data=aggregate_sentiment, alpha=0.5)
plt.plot(aggregate_sentiment['Net Price'], aggregate_sentiment['Predicted Rating'], color='red')
plt.title('Net Price vs Average Rating (Custom Regression Line)')
plt.xlabel('Net Price ($)')
plt.ylabel('Average Rating')
plt.show()
