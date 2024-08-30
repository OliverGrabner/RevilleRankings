import pandas as pd
data = pd.read_csv('combined.csv') 
unique_courses = data.iloc[:, 0].unique()
print(f"There are {len(unique_courses)} unique courses in the dataset.")
