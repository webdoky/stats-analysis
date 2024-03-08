import glob

from is_slug_in import is_slug_in


def get_initial_slugs() -> list:
    initial_slugs = []
    markdown_glob = glob.glob(
        './translated-content/files/**/*.md', recursive=True)
    for filepath in markdown_glob:
        content = open(filepath).read()
        frontmatter = content.split("---")[1]
        slug = frontmatter.split("slug: ")[1].split("\n")[0]
        if not is_slug_in(slug):
            continue
        initial_slugs.append(slug)
    return initial_slugs
