import os

import dotenv
from github import Auth, Github

dotenv.load_dotenv()
if os.getenv('GITHUB_TOKEN') is None:
    raise Exception('No GITHUB_TOKEN environment variable found')

auth = Auth.Token(os.getenv('GITHUB_TOKEN'))

# DISCUSSION_ID = 2858
DISCUSSION_ID = 2860
table_header = "| URL | Clicks |\n| --- | --- |"

def check_github():
    try:
        try:
            gh = Github(auth=auth)
        except:
            raise Exception('Invalid access token')
        gh.get_repo('webdoky/content').get_issue(DISCUSSION_ID)
    except:
        raise Exception('No discussion with the given ID found')

def get_markdown(weights):
    print(weights)
    return table_header + "\n" + "\n".join((f"| {weight[0]} | {weight[1]} |" for weight in weights if float(weight[1]) > 0.0))

def save_to_github(weights):
    with Github(auth=auth) as gh:
        repo = gh.get_repo('webdoky/content')
        discussion = repo.get_issue(DISCUSSION_ID)
        discussion.edit(body=get_markdown(weights))
    # gh.close()