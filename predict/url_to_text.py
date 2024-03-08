from get_slug_from_url import get_slug_from_url


def url_to_text(registry: dict, url: str):
    slug = get_slug_from_url(url)
    # return slug.replace("/", " ")
    if slug not in registry:
        print(f"Slug not found: {slug}")
        return ""
    return registry[slug]
