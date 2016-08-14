import markdown
import os


def markdown_to_html(file):
    """
    Преобразование markdown файла в html код
    """
    with open(file, 'r', encoding='utf-8') as f:
        all_file = ''
        for st in f.readlines():
            all_file += st
    html = markdown.markdown(all_file, extensions=['codehilite'])
    return html


def check_found_file(filename):
    """
    Проверка существования файла
    """
    if os.access(filename, os.F_OK):
        if os.access(filename, os.R_OK):
            return True
    return False

