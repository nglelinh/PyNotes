# coding=utf-8
import markdown


def markdown_to_html(filename, page_folder):
    """
    Преобразование markdown файла в html код
    """
    f = open(page_folder + '/' + filename + '.md', 'r')
    all_file = ''
    for st in f.readlines():
        all_file += st
    html = markdown.markdown(all_file.decode('utf8'), extensions=['codehilite'])
    return html


def check_found_file(filename):
    """
    Проверка существования файла
    """
    try:
        file = open(filename)
    except IOError as e:
        return False
    else:
        with file:
            return True
