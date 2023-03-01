import json
import os
import pandas as pd

# create empty list to store job data
job_data = []

# iterate through job data files and extract job information
for role_name in ["data scientist", "data analyst", "data engineer", "machine learning engineer"]:
    for company in ["apple", "google", "microsoft", "facebook", "tesla", "amazon", "UT Health Science Center at San Antonio"]:
        folder_path = f"raw_data/{role_name.replace(' ', '-')}/{company.replace(' ', '-')}"
        for filename in os.listdir(folder_path):
            with open(os.path.join(folder_path, filename), 'r') as f:
                job = json.load(f)
                job_data.append({
                    'id': job["id"],
                    'role': role_name,
                    'company': job["company"],
                    'description': job["description"]
                })

# create pandas DataFrame from job data
df = pd.DataFrame(job_data)

# print first few rows of the DataFrame
print(df.head())
