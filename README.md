# GitHub Issue Analyzer

This project is a data pipeline for fetching and analyzing GitHub issues. It provides functionality to fetch issues from a specified GitHub repository, save them to a CSV file, and perform various analyses on the issues.

## Features

- Fetch all issues from a GitHub repository using the GitHub API
- Save fetched issues to a CSV file
- Analyze the issues stored in a CSV file
- Count resolved and unresolved issues
- Calculate the average time to resolve an issue
- Generate visualizations of issue statistics
- Apply a category machine learning model to cluster and label the issues

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/github-issue-analyzer.git

2. Install the required dependencies:

```shell
pip install -r requirements.txt
```


3. Set up the configuration:

Create a config.env file in the project root directory.
Add the following environment variables to the config.env file:
OWNER: GitHub repository owner
REPO: GitHub repository name
API_REQUEST_TIMEOUT: Timeout for API requests (in seconds)

## Usage
Fetch and save GitHub issues:
```shell
python data-plane/aggregate.py
```


This will fetch all issues from the specified GitHub repository and save them to a CSV file (output/github_issues.csv).

## Analyze the GitHub issues:
```shell
python static-analyze/analyze.py
```


This will analyze the issues stored in the CSV file and generate visualizations of issue statistics.

Train the category machine learning model:
```shell
python category-ml/train.py
```

This will train the model using the GitHub issues and generate cluster labels for the issues.

## License
This project is licensed under the MIT License.See the LICENSE file for more information.

