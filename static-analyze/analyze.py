import pandas as pd
import matplotlib.pyplot as plt

def analyze_issues(csv_file):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Total number of issues
    total_issues = len(df)

    # Number of resolved issues
    resolved_issues = len(df[df['state'] == 'closed'])

    # Number of unresolved issues
    unresolved_issues = len(df[df['state'] == 'open'])

    # Average time taken to resolve an issue (if closed)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['closed_at'] = pd.to_datetime(df['closed_at'])
    df['time_to_resolve'] = (df['closed_at'] - df['created_at']).dt.days
    avg_time_to_resolve = df[df['state'] == 'closed']['time_to_resolve'].mean()

    # Visualizations
    labels = ['Resolved', 'Unresolved']
    sizes = [resolved_issues, unresolved_issues]
    colors = ['#66c2a5', '#fc8d62']
    explode = (0.1, 0)  # explode the 1st slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Resolved vs Unresolved Issues')
    plt.show()

    # More visualizations can be added as needed

    # Print the metrics
    print(f"Total issues: {total_issues}")
    print(f"Resolved issues: {resolved_issues}")
    print(f"Unresolved issues: {unresolved_issues}")
    print(f"Average time to resolve an issue: {avg_time_to_resolve} days")

# Example usage:
csv_file = "../output/argo-cd_issues.csv"
analyze_issues(csv_file)