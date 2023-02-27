import pandas as pd
import spacy
import os

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Create an empty list to store the job data
job_data = []

# Iterate through the raw_data folder and extract job information
for root, dirs, files in os.walk('raw_data'):
    for file in files:
        # Get the job data from the file
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            data = f.read().strip().split('\n')
        
        # Extract the job name, company, and description
        job_name = data[0]
        company = os.path.basename(root)
        description = ' '.join(data[1:])
        
        # Tokenize the job name and description using spaCy
        job_name_tokens = ' '.join([t.text.lower() for t in nlp(job_name)])
        description_tokens = ' '.join([t.text.lower() for t in nlp(description)])
        
        # Append the job data to the list
        job_data.append({
            'job_name': job_name_tokens,
            'id': os.path.splitext(file)[0],
            'company': company,
            'job_description': description_tokens
        })

# Create a pandas DataFrame from the job data
df = pd.DataFrame(job_data)

# Print the first few rows of the DataFrame
print(df.head())
