#!/usr/bin/env python3
import pandas as pd

from adjust_stats import adjust_stats
from create_registry import create_registry
from get_slug_from_url import get_slug_from_url
from predict import create_ctr_model, predict_ctr

def run():
    registry = create_registry()

    stats = pd.read_csv('./stats/Pages.csv')
    adjust_stats(registry, stats)
    model = create_ctr_model(stats)
    stats.sort_values(by="meta_CTR", ascending=False, inplace=True)
    initial_slugs = { get_slug_from_url(url) for url in stats["URL"].to_list() }
    # stats.to_csv('./stats/_Pages.csv', index=False)
    # print(predict_ctr(model, registry, "https://webdoky.org/uk/docs/Web/CSS/actual_value/"))

    # Create an empty pandas DataFrame
    empty_stats = pd.DataFrame(columns=["URL", "meta_CTR"])

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
        
        empty_stats = pd.concat([empty_stats, pd.DataFrame([{"URL": slug, "meta_CTR": prediction}])], ignore_index=True)

    empty_stats.sort_values(by="meta_CTR", ascending=False, inplace=True)
    empty_stats.to_csv('./stats/_PredictedPages.csv', index=False)

if __name__ == "__main__":
    run()