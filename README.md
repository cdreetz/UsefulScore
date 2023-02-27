# UsefulScore

## Goal
The goal is to determine how useful the programs and the courses are in terms of preparing students for the workforce.  It will be a direct comparison of what companies are wanting through the jobs that they post.  Both determining how useful the courses are for teaching the right skills but also getting a better understanding of the market needs for data based jobs.

## Plan

### Part 1
There are two main components required to accomplish this.  First the UTSA catalog will be read in via raw html, and parsed with Beautiful Soup.  Followed by cleaning up the html code to be text only and "prettified", and seperated to make up the individual course blocks containing titles and descriptions. The Spacy pretrained model and pipeline is used to run the text only strings to be tokenized and tagged.  The [en_core_web_sm] pipe used is described as "A small English pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities."


![image](https://user-images.githubusercontent.com/117322020/221216365-7db3f421-f203-4dd6-9a60-eec0a27ea31f.png)

### Part 2
Once the department program and course catalog has been processed with spaCy's nlp function, the same will be applied to relevant job posts and descriptions.  The type of jobs we want to compare are ones like Data Scientist, Data Analyst, Predictive Modeling, and possibly Business Analyst and Data Engingeer.
