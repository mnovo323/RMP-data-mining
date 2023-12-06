import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv('../data/school_student_ratings_sentiment_and_avg_rating.csv')

# drop rows with sentiment values of 0
df = df[df['Sentiment'] != 0]

# normalize the sentiment values
df['Sentiment'] = (df['Sentiment'] - df['Sentiment'].min()) / (df['Sentiment'].max() - df['Sentiment'].min())

# normalize the average rating values
df['Average Rating'] = (df['Average Rating'] - df['Average Rating'].min()) / (df['Average Rating'].max() - df['Average Rating'].min())

# find the correlation between the two columns
print(df['Average Rating'].corr(df['Sentiment']))

# draw the scatter plot with the linear regression line
plt.pyplot.figure(figsize=(12, 8))
sns.regplot(x='Average Rating', y='Sentiment', data=df)
plt.pyplot.title('Average Rating vs. Sentiment')
plt.pyplot.xlabel('Average Rating')
plt.pyplot.ylabel('Sentiment')
plt.pyplot.show()
