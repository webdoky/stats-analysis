import pandas as pd
from url_to_text import url_to_text

def adjust_stats(registry: dict, stats: pd.DataFrame) -> pd.DataFrame:
    # Synthetic value which indicates both number of clicks and clicks-shows ratio
    stats["meta_CTR"] = stats["Clicks"].divide(stats["Shows"]).multiply(stats["Clicks"])
    # convert "URL" field with url_to_text function
    stats["Text"] = stats["URL"].apply(lambda url: url_to_text(registry, url))
