from flask import Flask, render_template, request
from config_provider import ConfigProvider
import os
import function
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

config = ConfigProvider()


def get_page(name):
    file = os.path.join(config.pages_folder, name + '.md')
    if function.check_found_file(file):
        page = function.markdown_to_html(file)
    else:
        page = config.not_found_text
    return page

def get_docs(name):
    file = os.path.join(config.docs_folder, name + '.md')

    if function.check_found_file(file):
        page = function.markdown_to_html(file)
    else:
        page = config.not_found_text
    return page

def get_sidebar(startpath):
    sidebar = ''
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        if os.path.isfile(path):
            link = render_template(
                'side_link.html',
                path=request.url_map + '/' + item,
                name=item
                )
        else:
            link = render_template(
                'side_link.html',
                path=request.url_map + '/' + item,
                name=item
                )
        sidebar = sidebar + link
    return sidebar


@app.route('/', methods=['GET'])
def home():
    return render_template(
        'page.html',
        title=config.main_title,
        side=get_page(config.side_bar),
        content=get_page(config.start_page)
    )

@app.route('/notes', methods=['GET'])
def noteshome():
    return render_template(
        'page.html',
        title=config.main_title,
        side=get_sidebar(config.docs_folder),
        content=get_page(config.start_page)
    )


@app.route('/notes/<path:path>', methods=['GET'])
def page(path):

    return render_template(
        'page.html',
        title=config.main_title,
        side=get_sidebar(config.docs_folder),
        content=get_docs(path)
    )


if __name__ == '__main__':
    app.run(port=config.port)
