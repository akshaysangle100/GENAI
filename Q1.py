import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Convert 'OverDue' values to lowercase and compare to 'true'
overdue_tasks = df[df['OverDue'].astype(str).str.lower() == 'true']

# Get the total number of overdue tasks
total_overdue_tasks = len(overdue_tasks)

# Report the total number of tasks that are overdue
print(f'Total number of tasks that are overdue: {total_overdue_tasks}')
