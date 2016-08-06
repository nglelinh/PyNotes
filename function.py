# coding=utf-8
import markdown
from config_provider import ConfigProvider

config = ConfigProvider


def markdown_to_html(filename):
    """
    Преобразование markdown файла в html код
    """
    f = open(config.pages_folder + '/' + filename + '.md', 'r')
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
