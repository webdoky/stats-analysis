#!/usr/bin/env python3
import os

import dotenv
from github import Auth, Github

from label_update import label_update

dotenv.load_dotenv()
if os.getenv('CONTENT_GITHUB_TOKEN') is None:
    raise Exception('No CONTENT_GITHUB_TOKEN environment variable found')

auth = Auth.Token(os.getenv('CONTENT_GITHUB_TOKEN'))

with Github(auth=auth) as gh:
    repo = gh.get_repo('webdoky/content')
    update_pull_requests = (pull for pull in repo.get_pulls(
        state='open', base='master') if pull.title.startswith("update"))
    for update_pull_request in update_pull_requests:
        label_update(update_pull_request)
