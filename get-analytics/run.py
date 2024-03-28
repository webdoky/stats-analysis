#!/usr/bin/env python3
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

GOOGLE_KEY = os.getenv('GOOGLE_KEY')
keyFile = './key.json'
scopes = ['https://www.googleapis.com/auth/webmasters.readonly']


def getYYYYMMDD(date):
    return date.strftime("%Y-%m-%d")


aWeek = timedelta(days=7).total_seconds()
target_period = timedelta(days=30*3).total_seconds()


def fileExists(path):
    return os.path.isfile(path)


def stripDomainFromUrl(url):
    return url.replace('https?:\/\/[^/]+', '').replace('/$', '')


if not GOOGLE_KEY:
    if not fileExists(keyFile):
        raise Exception('No key file or GOOGLE_KEY environment variable found')
    GOOGLE_KEY = open(keyFile, 'r').read()

if not fileExists(keyFile):
    with open(keyFile, 'w') as f:
        f.write(GOOGLE_KEY)

credentials = service_account.Credentials.from_service_account_file(
    keyFile, scopes=scopes)

# Getting analytics from Google
searchConsoleClient = build('webmasters', 'v3', credentials=credentials)


endTimestamp = datetime.now().timestamp() - aWeek
print('endTimestamp', endTimestamp)
startTimestamp = endTimestamp - target_period
print('startTimestamp', startTimestamp)

response = searchConsoleClient.searchanalytics().query(
    siteUrl='sc-domain:webdoky.org',
    body={
        'startDate': getYYYYMMDD(datetime.fromtimestamp(startTimestamp)),
        'endDate': getYYYYMMDD(datetime.fromtimestamp(endTimestamp)),
        'dimensions': ['PAGE'],
        'metrics': ['engagedSessions']
    }).execute()
# print(response)

records = response.get('rows', [])

# Processing and saving analytics data
weights = []

for record in records:
    keys, impressions = record['keys'], record['impressions']
    for url in keys:
        weights.append({
            'URL': stripDomainFromUrl(url),
            'Impressions': impressions
        })

# Save to file
with open('./_Pages.json', 'w') as f:
    f.write(json.dumps(weights))
