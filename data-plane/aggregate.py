import requests
import csv
import time
from dotenv import load_dotenv, find_dotenv , dotenv_values

# reading config from config.env
def config():

    conf = dotenv_values(find_dotenv("config.env"))
    if conf is not None :
        return conf
    return "config not found!"

# making config file available as a dict
cnf = config()

def fetch_all_issues(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    params = {"state": "all", "per_page": 100}  # Adjust per_page as needed
    issues = []

    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            fetched_issues = response.json()
            issues.extend(fetched_issues)
            if "next" in response.links:
                url = response.links["next"]["url"]
                # Add a delay to avoid hitting rate limits
                time.sleep(int(cnf["API_REQUEST_TIMEOUT"]))  # Adjust as needed
            else:
                break
        else:
            print(f"Failed to fetch issues. Status code: {response.status_code}")
            break

    return issues

def save_issues_to_csv(issues, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "body", "labels", "state", "created_at", "closed_at"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow({
                "id": issue["id"],
                "title": issue["title"],
                "body": issue["body"],
                "labels": issue["labels"],
                "state": issue["state"],
                "created_at": issue["created_at"],
                "closed_at": issue.get("closed_at", "")  # handle cases where issue is not closed
            })

# Example usage:
repo_owner = cnf["OWNER"]
repo_name = cnf["REPO"]
issues = fetch_all_issues(repo_owner, repo_name)
save_issues_to_csv(issues, "../output/github_issues.csv")
