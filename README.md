# UsefulScore

## Goal
The goal is to determine how useful the programs and the courses are in terms of preparing students for the workforce.  It will be a direct comparison of what companies are wanting through the jobs that they post.  Both determining how useful the courses are for teaching the right skills but also getting a better understanding of the market needs for data based jobs.

## Plan

### Part 1
There are two main components required to accomplish this.  First the UTSA catalog will be read in via raw html, and parsed with Beautiful Soup.  Followed by cleaning up the html code to be text only and "prettified", and seperated to make up the individual course blocks containing titles and descriptions. The Spacy pretrained model and pipeline is used to run the text only strings to be tokenized and tagged.  The [en_core_web_sm] pipe used is described as "A small English pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities."


![image](https://user-images.githubusercontent.com/117322020/221216365-7db3f421-f203-4dd6-9a60-eec0a27ea31f.png)

### Part 2
Once the department program and course catalog has been processed with spaCy's nlp function, the same will be applied to relevant job posts and descriptions.  The type of jobs we want to compare are ones like Data Scientist, Data Analyst, Predictive Modeling, and possibly Business Analyst and Data Engingeer.


# File Descriptions

### Jobscraper.py
The web scraper utilized to collect data from the job postings of interest.  Built primarily off of Selenium tools from the driver to scrollIntoView method.  Directed by XPATH's for clicking, scrolling, and recording data.

### Bot.py
This script sets up the settings of the webdriver in which Jobscraper.py works within.  Defines some of the methods used in Jobscraper as well.


### Data.py

The 4 columns in the Pandas DataFrame "df" are:
```
"id" - This column contains the job ID, which is a unique identifier for each job.
"role" - This column contains the role name, which specifies the job position such as "data scientist", "data analyst", "data engineer", or "machine learning engineer".
"company" - This column contains the name of the company that posted the job.
"description" - This column contains the job description, which provides details about the responsibilities, requirements, and qualifications for the job.
phrases = ["Excel", "SQL", "R", "data mining", "python", "java", "machine learning", "ML", "natural language processing", "NLP", "deep learning", "data analytics", "predictive modeling", "forecasting", "business", "statistical analysis", "KPI", "artificial intelligence", "AI", "statistical modeling", "data management", "algorithms", "automation", "TensorFlow", "PyTorch", "big data", "SAS", "survival analysis", "time series", "inference", "Power BI", "Tableau"]
```

### Dataexample.ipynb
A notebook that demonstrates what kind of data can be found in the Pandas dataframe named df, which is also referenced in Data.py.  Also begins to demonstrate the application of spacy nlp function for tokenizing the contents of each job description.  For loops are used to demonstrate the occurance of phrases within the descriptions rather than using the nlp function due to for loops just being faster.   The example output below shows us the respective percentages in which each phrase is found from all of the recorded job descriptions: "Business" being referred to in 69% of all descriptions, "ML" being referred to in 68% of all descriptions.
```
business: 69.29%
ML: 68.46%
python: 61.00%
```

### GraduateCatalog.ipynb
A notebook that utilizes BeautifulSoup to parse the html code of my university's graduate course catalog, containing the available course names and course descriptions.  Because bs4 "prettyify" transforms the html to very reading friendly text, we can use spacy nlp function to tokenize the descriptions, and then search for any given phrase or word by searching the token.text elements created by using the nlp function.  

### Webapp.py 
The beginning of a script that uses the Python Dash framework to create a web application.  While unfinished it will eventually display the results demonstrated in the Dataexample notebook, allowing users to view the percentage of occurance of any of the phrases, while having the option to select all 4 roles, or viewing the phrases per individual role name.  
