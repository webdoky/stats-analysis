#!/usr/bin/env python3
import os

import dotenv
from github import Auth, Github

from label_translation import label_translation

dotenv.load_dotenv()
if os.getenv('CONTENT_GITHUB_TOKEN') is None:
    raise Exception('No CONTENT_GITHUB_TOKEN environment variable found')

auth = Auth.Token(os.getenv('CONTENT_GITHUB_TOKEN'))

with Github(auth=auth) as gh:
    repo = gh.get_repo('webdoky/content')
    translation_pull_requests = (pull for pull in repo.get_pulls(state='open', base='master') if pull.title.startswith("translation"))
    for translation_pull_request in translation_pull_requests:
        label_translation(translation_pull_request)
    