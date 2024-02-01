import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read CSV file into a DataFrame
df = pd.read_csv("../output/github_issues.csv")

# Combine the title and body columns into a single text column
df['text'] = df['title'] + df['body']
df['text'].fillna('', inplace=True)

# Split the data into training and testing sets
train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

# Vectorize the text data using the Bag-of-Words model
vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_data['text'])
test_vectors = vectorizer.transform(test_data['text'])

# Train a Naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(train_vectors, train_data['labels'])

# Test the classifier on the testing data
test_predictions = clf.predict(test_vectors)

# Calculate the accuracy of the classifier
accuracy = clf.score(test_vectors, test_data['labels'])

print(f"Accuracy: {accuracy}")
