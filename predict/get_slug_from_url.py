
def get_slug_from_url(url: str) -> str:
    # Remove hash from URL
    url = url.split("#")[0]
    path = url.replace("https://webdoky.org/uk/docs/",
                       "").replace("https://webdoky.org/", "")
    if path.endswith("/"):
        path = path[:-1]
    return path
