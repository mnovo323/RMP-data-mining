import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# fixes weird mac issue with python ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


nltk.download('vader_lexicon')

df = pd.read_csv('../data/school_student_ratings.csv')
df.dropna(subset=['Comment'], inplace=True)
df = df[df['Comment'].str.strip() != '']

sia = SentimentIntensityAnalyzer()

def get_sentiment(comment):
    return sia.polarity_scores(comment)['compound']

df['Sentiment'] = df['Comment'].apply(get_sentiment)

res_df = df[['School ID', 'Average Rating', 'Sentiment']]

res_df.to_csv('../data/school_student_ratings_sentiment_and_avg_rating.csv', index=False)

print('Sentiment analysis completed and saved as school_student_ratings_sentiment_and_avg_rating.csv')