#!/usr/bin/env python3
import json
import os

import dotenv
from github import Auth, Github

dotenv.load_dotenv()
if os.getenv('STATS_GITHUB_TOKEN') is None:
    raise Exception('No STATS_GITHUB_TOKEN environment variable found')

auth = Auth.Token(os.getenv('STATS_GITHUB_TOKEN'))

ISSUE_ID = 1
table_header = "| URL | Clicks |\n| --- | --- |"

def get_markdown(weights):
    print(weights[0])
    return table_header + "\n" + "\n".join((f"| https://developer.mozilla.org/en-us/docs/{weight['URL']} | {weight['Clicks']} |" for weight in weights if weight['Clicks'] > 0.0))

weights_data = open('./_Prediction.json').read()
weights = json.loads(weights_data)

with Github(auth=auth) as gh:
    repo = gh.get_repo('webdoky/stats-analysis')
    issue = repo.get_issue(ISSUE_ID)
    issue.edit(body=get_markdown(weights))