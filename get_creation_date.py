import glob

from get_file_creation_date import get_file_creation_date
from is_slug_in import is_slug_in

registry = {}
markdown_glob = glob.glob('./translated-content/files/**/*.md', recursive=True)
for filepath in markdown_glob:
    content = open(filepath).read()
    frontmatter = content.split("---")[1]
    slug = frontmatter.split("slug: ")[1].split("\n")[0]
    if not is_slug_in(slug):
        continue
    print('creation date init', slug)
    # Get file creation date from git
    registry[slug] = get_file_creation_date(filepath)

def get_creation_date(slug: str) -> str | None:
    return registry[slug] if slug in registry else None