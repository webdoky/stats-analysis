
def get_slug_from_url(url: str) -> str:
    path= url.replace("https://webdoky.org/uk/docs/", "").replace("https://webdoky.org/", "")
    if path.endswith("/"):
        path = path[:-1]
    return path