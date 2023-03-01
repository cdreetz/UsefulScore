import dash
from dash import dcc
from dash import html
import json
import os
import pandas as pd
import plotly.express as px
from collections import Counter
import re



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

# Define a dictionary of abbreviations
abbreviations = {
    "machine learning": "ML",
    "artificial intelligence": "AI",
    "natural language processing": "NLP"
}

# Define a list of phrases to search for
phrases = ["Excel", "SQL", "R", "data mining", "python", "java", "machine learning", "ML", "natural language processing", "NLP", "deep learning", "data analytics", "predictive modeling", "forecasting", "business", "statistical analysis", "KPI", "artificial intelligence", "AI", "statistical modeling", "data management", "algorithms", "automation", "TensorFlow", "PyTorch", "big data", "SAS", "survival analysis", "time series", "inference", "Power BI", "Tableau"]

# Create a counter object to count the number of descriptions that contain each phrase
phrase_count = Counter()

# Iterate through each description and count the number of phrases it contains
for desc in df["description"].values:
    desc_phrases = set()
    for phrase in phrases:
        if re.search(rf"\b{phrase}\b", desc, re.IGNORECASE):
            desc_phrases.add(phrase)
    for phrase in desc_phrases:
        if phrase in abbreviations:
            phrase = abbreviations[phrase]
        phrase_count[phrase] += 1

# Print the phrases and the percentage of descriptions that contain them in descending order
total_count = len(df)

for phrase, count in phrase_count.most_common():
    score = count / total_count

# Define the list of job roles to display
roles = list(df['role'].unique())








# Create a Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    # Create a dropdown menu to select the job role
    html.Label('Job Role:'),
    dcc.Dropdown(
        id='role-dropdown',
        options=[{'label': r, 'value': r} for r in roles],
        value=roles[0]
    ),
    # Create a plot to display the phrase percentages
    dcc.Graph(id='phrase-plot')
])

# Define the app callback
@app.callback(
    dash.dependencies.Output('phrase-plot', 'figure'),
    [dash.dependencies.Input('role-dropdown', 'value')]
)
def update_plot(selected_role):
    # Filter the DataFrame by the selected job role
    filtered_df = df[df['role'] == selected_role]
    
    # Calculate the phrase percentages for the filtered DataFrame
    phrase_counts = filtered_df['description'].str.count('|'.join(phrases), re.IGNORECASE)
    total_counts = filtered_df['description'].str.len() - filtered_df['description'].str.count('\s')
    phrase_percentages = phrase_counts / total_counts * 100
    
    # Create a bar chart to display the phrase percentages
    fig = px.bar(
        x=phrases,
        y=phrase_percentages,
        labels={'x': 'Phrase', 'y': 'Percentage'},
        title=f'Phrase Percentages for {selected_role}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)