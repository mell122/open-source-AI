import requests
import csv
import time

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
                time.sleep(5)  # Adjust as needed
            else:
                break
        else:
            print(f"Failed to fetch issues. Status code: {response.status_code}")
            break

    return issues

def save_issues_to_csv(issues, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "state", "created_at", "closed_at"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for issue in issues:
            writer.writerow({
                "id": issue["id"],
                "title": issue["title"],
                "state": issue["state"],
                "created_at": issue["created_at"],
                "closed_at": issue.get("closed_at", "")  # handle cases where issue is not closed
            })

# Example usage:
repo_owner = "numpy"
repo_name = "numpy"
issues = fetch_all_issues(repo_owner, repo_name)
save_issues_to_csv(issues, "output/github_issues.csv")
