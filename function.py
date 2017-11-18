import markdown
import os


def markdown_to_html(file):
    with open(file, 'r') as f:
        all_file = ''
        for st in f.readlines():
            all_file += st
    html = markdown.markdown(all_file, extensions=['codehilite'])
    return html


def check_found_file(filename):
    if os.access(filename, os.F_OK):
        if os.access(filename, os.R_OK):
            return True
    return False

