import json

def get_path_from_slug(slug: str) -> str:
    return slug.lower().replace('::', '_doublecolon_').replace(':', '_colon_').replace('*', '_star_')

data = open('./_Prediction.json').read()
weights = json.loads(data)
registry = {get_path_from_slug(weight["URL"]): weight["Clicks"] for weight in weights}
# print(registry)

def get_predicted_popularity(slug: str) -> float:
    return registry.get(slug, 0.0)