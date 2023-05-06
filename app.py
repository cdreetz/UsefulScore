from flask import Flask
from processing import print_job_post_stats

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    stats = print_job_post_stats
    return "<p>{stats}</p>"
