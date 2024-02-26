#!/usr/bin/env python3
from datetime import datetime, timedelta

import pandas as pd

from adjust_stats import adjust_stats
from create_registry import create_registry
from get_initial_slugs import get_initial_slugs
from predict import create_ctr_model, predict_ctr

THREE_MONTHS_AGO = str(datetime.now() - timedelta(days=90))

def run():
    registry = create_registry()

    stats = pd.read_csv('./stats/Pages.csv')
    # Remove pages newer than 3 months
    adjust_stats(registry, stats)
    stats = stats[stats["Date"] < THREE_MONTHS_AGO]
    model = create_ctr_model(stats)
    stats.sort_values(by="Clicks", ascending=False, inplace=True)
    initial_slugs = get_initial_slugs()
    # stats.to_csv('./stats/_Pages.csv', index=False)
    # print(predict_ctr(model, registry, "https://webdoky.org/uk/docs/Web/CSS/actual_value/"))

    # Create an empty pandas DataFrame
    empty_stats = pd.DataFrame(columns=["URL", "Clicks"])

    # Read Markdown filepaths in ./content/files into list
    # markdown_glob = glob.glob('./content/files/**/*.md', recursive=True)
    # Iterate over markdown filepaths
    for slug in registry:
        if slug in initial_slugs:
            continue
        # Get "slug" field from frontmatter
        # frontmatter = open(filepath).read().split("---")[1]
        # slug = frontmatter.split("slug: ")[1].split("\n")[0]
        prediction = predict_ctr(model, registry, slug)
        
        print(f"URL: {slug}, CTR: {prediction}")
        
        empty_stats = pd.concat([empty_stats, pd.DataFrame([{"URL": slug, "Clicks": prediction}])], ignore_index=True)

    empty_stats.sort_values(by="Clicks", ascending=False, inplace=True)
    empty_stats.to_csv('./stats/_PredictedPages.csv', index=False)

if __name__ == "__main__":
    run()