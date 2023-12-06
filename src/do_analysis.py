import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('../data/school_aggregate_sentiment_rating_average_cost_median_salary.csv')

# Drop rows with 0.0 sentiment
df = df[df['Average Sentiment'] != 0.0]

# Calculate and print correlation matrix
correlation_matrix = df[['Median Salary', 'Net Price', 'Average Rating', 'Average Sentiment']].corr()
print(correlation_matrix)

# Create pair plot
sns.pairplot(df[['Median Salary', 'Net Price', 'Average Rating', 'Average Sentiment']])
plt.show()
