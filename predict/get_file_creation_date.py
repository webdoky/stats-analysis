import os.path
import subprocess


def get_file_creation_date(filepath: str) -> str:
    path_components = filepath.split("/")
    path_components.remove(".")
    folder = os.path.abspath("./" + path_components[0])
    relative_filepath = "/".join(path_components[1:])
    # print(f"Getting creation date for {filepath} in {folder}")
    creation_date_str = subprocess.check_output(
        ['git', 'log', '--diff-filter=A', '-1', '--format=%ad', '--date=iso', '--', relative_filepath], cwd=folder).decode('utf-8').strip()
    if not creation_date_str:
        print(f"Creation date not found for {filepath}")
    return creation_date_str
