
SECTIONS_IN = [
    "Glossary",
    "Web/HTML",
    "Web/CSS",
    "Web/JavaScript",
    "Web/SVG"
]


def is_slug_in(slug):
    if slug == "Web":
        return True
    # return True
    for section in SECTIONS_IN:
        if slug.startswith(section):
            return True
    return False
