import pandas as pd

from get_creation_date import get_creation_date
from get_slug_from_url import get_slug_from_url
from url_to_text import url_to_text


def adjust_stats(registry: dict, stats: pd.DataFrame) -> pd.DataFrame:
    # convert "URL" field with url_to_text function
    stats["Text"] = stats["URL"].apply(lambda url: url_to_text(registry, url))
    stats["Date"] = stats["URL"].apply(
        lambda url: get_creation_date(get_slug_from_url(url)))
