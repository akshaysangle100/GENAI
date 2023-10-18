import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Convert the 'OverDue' column values to lowercase strings
df['OverDue'] = df['OverDue'].astype(str).str.lower()

# Group the data by 'project' and count the number of overdue tasks in each group
overdue_tasks_by_project = df[df['OverDue'] == 'true'].groupby('project').size()

# Create a bar chart
overdue_tasks_by_project.plot(kind='bar', figsize=(12, 6))
plt.title('Total Overdue Tasks by Project')
plt.xlabel('Project')
plt.ylabel('Total Overdue Tasks')

# Display the bar chart
plt.show()
