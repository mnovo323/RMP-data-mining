import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns

sentiment = pd.read_csv('../data/school_student_ratings_sentiment_and_avg_rating.csv')
ratings = pd.read_csv('../data/school_student_ratings.csv')
schools = pd.read_csv('../data/school.csv')
rmp_boe_mapping = pd.read_csv('../data/rmp_board_of_ed_mapping.csv')
# bring in boe data, but only the columns we need
boe = pd.read_csv('../data/Most-Recent-Cohorts-Institution.csv', usecols=['UNITID', 'MD_EARN_WNE_P10', 'COSTT4_A', 'NPT4_PUB', 'NPT4_PRIV'])

# get single net price column
boe['Net Price'] = boe['NPT4_PUB'].fillna(0) + boe['NPT4_PRIV'].fillna(0)
boe['Net Price'] = boe['Net Price'].replace(0, np.nan)  # Assuming that a value of 0 means missing data

# make aggregate sentiment dataframe, aggregating sentiment and average rating by school id
aggregate_sentiment = sentiment.groupby('School ID', as_index=False)[['Average Rating', 'Sentiment']].mean()

# rename rmp_boe_mapping column for merging
rmp_boe_mapping.columns = ['School ID', 'Board of Education School ID']

# create dataframe with school id, median salary, and average cost using the rmp_boe_mapping
aggregate_sentiment = aggregate_sentiment.merge(rmp_boe_mapping, on='School ID', how='left')
aggregate_sentiment = aggregate_sentiment.merge(boe[['UNITID', 'MD_EARN_WNE_P10', 'COSTT4_A', 'Net Price']], left_on='Board of Education School ID', right_on='UNITID', how='left')



# create a new dataframe with only school id, median salary, average cost, average rating, and average sentiment
aggregate_sentiment = aggregate_sentiment[['School ID', 'UNITID', 'MD_EARN_WNE_P10', 'COSTT4_A', 'Net Price', 'Average Rating', 'Sentiment']]

# drop rows with null values
aggregate_sentiment.dropna(inplace=True)

# take logs of median salary and average cost
aggregate_sentiment['Log Median Salary'] = np.log1p(aggregate_sentiment['MD_EARN_WNE_P10'])
aggregate_sentiment['Log Average Cost'] = np.log1p(aggregate_sentiment['COSTT4_A'])
aggregate_sentiment['Log Net Price'] = np.log1p(aggregate_sentiment['Net Price'])

# rename columns
aggregate_sentiment.columns = ['School ID', 'Board of Education School ID', 'Median Salary',  'Average Cost', 'Net Price', 'Average Rating', 'Average Sentiment', 'Log Median Salary', 'Log Average Cost', 'Log Net Price']

# write to csv
aggregate_sentiment.to_csv('../data/school_aggregate_sentiment_rating_average_cost_median_salary.csv', index=False)