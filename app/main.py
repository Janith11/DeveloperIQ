import requests
from fastapi import FastAPI
from datetime import datetime, timedelta
import time

app= FastAPI()
USER_NAME = "Janith11"
@app.get("/")
def index():
    return {"details": "Hello World!"}



# GitHub API credentials
github_username = 'Janith11'
github_token = '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'
organization =  'final-projet'

OWNER           =   'Janith11'
REPO            =  'angular-new'



@app.get("/details")
def get_user_details():

    COMMENTS_URI    =   f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    ISSUES_URI      =   f"https://api.github.com/repos/{OWNER}/{REPO}/issues/comments"
    ACTIVITY_URI    =   f"https://api.github.com/repos/{OWNER}/{REPO}/stats/commit_activity"

    # repository_contributors_url = f"https://api.github.com/repos/{organization}/{repo}/contributors"
    # contributors = requests.request("GET",repository_contributors_url,auth=(USER_NAME,github_token))
    contributors = requests.request("GET",COMMENTS_URI,auth=(USER_NAME,github_token))
    print(contributors)
    return contributors.json()

    # List of contributors to GitHub REST API
    # contributors = ['Kasuntharu', 'thushanwithanage', 'Janith11']

     # Get yesterday's date
    # yesterday = datetime.now() - timedelta(days=1)
    # yesterday_str = yesterday.strftime('%Y-%m-%d')

    # for contributor in contributors:
    # GitHub API endpoint for contributor events
        # github_api_url = f'https://api.github.com/users/{contributor}/events'

        # GitHub API request headers
        # headers = {
            # 'Authorization': f'Basic {github_username}:{github_token}'
        # }

        # Make GitHub API request
        # response = requests.get(github_api_url, headers=headers)

    # return  response.json()