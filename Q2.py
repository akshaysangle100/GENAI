import pandas as pd

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

# Report the total number of open and closed tasks by each task group
print("Total Open Tasks:")
print(task_group_counts['Open'])

print("\nTotal Closed Tasks:")
print(task_group_counts['Closed'])
