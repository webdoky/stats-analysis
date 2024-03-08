
SECTIONS_IN = [
    "Glossary",
    "Web/HTML",
    "Web/CSS",
    "Web/JavaScript",
    "Web/SVG"
]


def is_slug_in(slug):
    # return True
    for section in SECTIONS_IN:
        if slug.startswith(section):
            return True
    return False
