import json
import os
import pandas as pd

__all__ = ['df', 'df_with_dummies']


# Create an empty list to store the job data
job_data = []

# Iterate through job data files and extract job information
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

# Create a pandas DataFrame from the job data
df = pd.DataFrame(job_data)

# Define a list of phrases to search for
phrases = ["Excel", "SQL", "R", "data mining", "python", "java", "machine learning", "ML", "natural language processing", "NLP", "deep learning", "data analytics", "predictive modeling", "forecasting", "business", "statistical analysis", "KPI", "artificial intelligence", "AI", "statistical modeling", "data management", "algorithms", "automation", "TensorFlow", "PyTorch", "big data", "SAS", "survival analysis", "time series", "inference", "Power BI", "Tableau"]

# Create a copy of the original dataframe
df_with_dummies = df.copy()

# Iterate through each phrase in the list and create a new column in the dataframe
for phrase in phrases:
    df_with_dummies[phrase] = df_with_dummies['description'].str.contains(phrase, case=False).astype(int)

