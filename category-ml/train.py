import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score
from joblib import dump

# Step 1: Data Collection (Assuming you already have your dataset)

# Step 2: Data Preprocessing
# Load dataset
data = pd.read_csv('../output/argo-cd_issues.csv')

# Clean data
data.drop_duplicates(inplace=True)
data.dropna(subset=['title', 'body'], inplace=True)

# Concatenate relevant columns into a single text column
data['text'] = data['title'] + ' ' + data['body'] + ' ' + data['labels']

# Step 3: Model Training
# Define the number of clusters
num_clusters = 13

# Create a pipeline with TF-IDF vectorizer and K-means clustering
pipeline = make_pipeline(
    TfidfVectorizer(stop_words='english'),
    KMeans(n_clusters=num_clusters, random_state=42)
)

# Train the model
pipeline.fit(data['text'])

# Save the trained model
dump(pipeline, 'model/github_issues.joblib')

# Step 4: Cluster Assignment
cluster_labels = pipeline.predict(data['text'])

# Step 5: Counting and Aggregation
cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()
total_issues = len(data)
cluster_percentages = (cluster_counts / total_issues) * 100

# Step 6: Labeling
category_labels = {
    0: "Missing Content",
    1: "Unclear Instructions",
    2: "Discuss Methodology",
    3: "Extension",
    4: "Runtime Error",
    5: "Discuss Implementation",
    6: "Fail to Replicate",
    7: "Enhancement",
    8: "Abnormal Behavior",
    9: "Paper-Code Misalignment",
    10: "Supplementary Information",
    11: "Re-implementation",
    12: "Others"
}

# Step 7: Formatting Output
output = pd.DataFrame({
    'ID': cluster_counts.index + 1,
    'Category': [category_labels[i] for i in cluster_counts.index],
    'No.': cluster_counts.values,
    'Rate': cluster_percentages.values.round(2)
})

# Print the formatted output
print(output)
