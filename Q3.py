import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Define a function to categorize tasks as 'Open' or 'Closed' based on cell values (case-insensitive)
def categorize_status(cell):
    cell_lower = cell.lower()  # Convert the cell value to lowercase
    if 'open' in cell_lower:
        return 'Open'
    elif 'close' in cell_lower:
        return 'Closed'
    else:
        return 'Other'

# Apply the categorize_status function to the 'Status' column to create a new 'Categorized Status' column
df['Categorized Status'] = df['Status'].apply(categorize_status)

# Group the data by 'Task Group' and 'Categorized Status' and count the number of tasks in each group
task_group_counts = df.groupby(['Task Group', 'Categorized Status']).size().unstack(fill_value=0)

# Drop the 'Other' column from the DataFrame if it exists
if 'Other' in task_group_counts.columns:
    task_group_counts.drop('Other', axis=1, inplace=True)

# Create a bar chart
task_group_counts.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Total Open and Closed Tasks by Task Group')
plt.xlabel('Task Group')
plt.ylabel('Total Tasks')
plt.legend(title='Status')

# Display the bar chart
plt.show()
