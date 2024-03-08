import json


def get_path_from_url(url: str) -> str:
    print(url)
    return url.split('/uk/docs/')[1].rstrip('/').lower().replace('::', '_doublecolon_').replace(':', '_colon_').replace('*', '_star_')


data = open('./_Pages.json').read()
weights = json.loads(data)
registry = {get_path_from_url(weight["URL"]): weight["Impressions"]
            for weight in weights if weight["URL"].startswith('https://webdoky.org/uk/docs/')}
# print(registry)


def get_popularity(slug: str) -> float:
    return registry.get(slug, 0.0)
