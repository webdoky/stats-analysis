import glob

from get_file_creation_date import get_file_creation_date
from is_slug_in import is_slug_in

registry = {}
markdown_glob = glob.glob('./translated-content/files/**/*.md', recursive=True)
print('creation date init')
for filepath in markdown_glob:
    content = open(filepath).read()
    frontmatter = content.split("---")[1]
    slug = frontmatter.split("slug: ")[1].split("\n")[0]
    if not is_slug_in(slug):
        continue
    # Get file creation date from git
    registry[slug] = get_file_creation_date(filepath)
print('creation date init done')


def get_creation_date(slug: str) -> str | None:
    creation_date = registry[slug] if slug in registry else None
    # if creation_date is None:
    #     raise ValueError(f"Creation date not found for {slug}")
    print(f"Creation date for {slug}: {creation_date}")
    return creation_date
