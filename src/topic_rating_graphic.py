import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Load your dataset with topics
data = pd.read_csv('../data/school_student_ratings_with_topics.csv')

# Assuming you have an 'Average Rating' column that represents the rating levels (e.g., 1 to 5)
# You can customize this based on your dataset structure
rating_col = 'Average Rating'

# Convert the 'Topics' column from string to a list of tuples
data['Topics'] = data['Topics'].apply(ast.literal_eval)

# Create an empty list to store DataFrames
dfs = []

# Iterate through each row and extract topic proportions and rating
for index, row in data.iterrows():
    for topic_id, proportion in row['Topics']:
        df = pd.DataFrame({'Rating': [row[rating_col]], 'Topic': [topic_id], 'Proportion': [proportion]})
        dfs.append(df)

# Concatenate the list of DataFrames into one DataFrame
topic_distribution = pd.concat(dfs, ignore_index=True)

# Aggregate the data by taking the mean of 'Proportion' for duplicate entries
topic_distribution = topic_distribution.groupby(['Rating', 'Topic'], as_index=False)['Proportion'].mean()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(topic_distribution.pivot(index='Rating', columns='Topic', values='Proportion'), cmap='coolwarm', annot=True, fmt='.2f', cbar=True)
plt.title('Topic Distribution by Ratings')
plt.xlabel('Topic')
plt.ylabel('Rating')
plt.show()
