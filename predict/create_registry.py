
import glob

from is_slug_in import is_slug_in
from markdown_to_text import markdown_to_text

def create_registry() -> dict:
    print('create_registry')
    registry = {}
    markdown_glob = glob.glob('./content/files/**/*.md', recursive=True)
    for filepath in markdown_glob:
        content = open(filepath).read()
        frontmatter = content.split("---")[1]
        slug = frontmatter.split("slug: ")[1].split("\n")[0]
        if not is_slug_in(slug):
            continue
        # Render Markdown to plain text
        text = markdown_to_text(content)
        registry[slug] = text
    print('create_registry done')
    return registry
    