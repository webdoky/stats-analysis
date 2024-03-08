import subprocess


def get_file_creation_date(filepath: str) -> str:
    return subprocess.check_output(['git', 'log', '-1', '--format=%cd', '--', filepath]).decode('utf-8').strip()
