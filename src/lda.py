import pandas as pd
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import preprocess_string, STOPWORDS

# Load your CSV data
data = pd.read_csv('../data/school_student_ratings.csv')

# drop rows with missing values in comment column
data = data.dropna(subset=['Comment'])

# Extract comments from the dataset
comments = data['Comment'].dropna().tolist()

# Preprocess the text (tokenization, lowercase, removing stopwords, etc.)
def preprocess_text(text):
    custom_stopwords = set(["school", "student", "teacher", "class"])  # Add custom stopwords
    words = preprocess_string(text)
    words = [word for word in words if word not in STOPWORDS and word not in custom_stopwords]
    return words

processed_comments = [preprocess_text(comment) for comment in comments]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(processed_comments)
corpus = [dictionary.doc2bow(comment) for comment in processed_comments]

# Train the LDA model
num_topics = 7  # You can adjust the number of topics as needed
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=20)

# Print the topics
for topic_id, topic_words in lda_model.print_topics():
    print(f"Topic {topic_id + 1}: {topic_words}")

# Assign topics to comments
topics = [lda_model[comment] for comment in corpus]

# Add the topics to the dataset
data['Topics'] = topics

# Save the modified dataset with topics
data.to_csv('../data/school_student_ratings_with_topics.csv', index=False)
