#!/usr/bin/env python3
import json
import os

import dotenv
from github import Auth, Github

dotenv.load_dotenv()
if os.getenv('GITHUB_TOKEN') is None:
    raise Exception('No GITHUB_TOKEN environment variable found')

auth = Auth.Token(os.getenv('GITHUB_TOKEN'))

DISCUSSION_ID = 1
table_header = "| URL | Clicks |\n| --- | --- |"

def get_markdown(weights):
    print(weights[0])
    return table_header + "\n" + "\n".join((f"| https://webdoky.org/uk/docs/{weight['URL']} | {weight['Clicks']} |" for weight in weights if weight['Clicks'] > 0.0))

weights_data = open('./_Prediction.json').read()
weights = json.loads(weights_data)

with Github(auth=auth) as gh:
    repo = gh.get_repo('webdoky/stats-analysis')
    discussion = repo.get_issue(DISCUSSION_ID)
    discussion.edit(body=get_markdown(weights))