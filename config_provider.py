import configparser as ConfigParser
import function


class ConfigProvider:
    config_file_name = 'config.ini'
    start_page = 'start'
    side_bar = 'sidebar'
    pages_folder = 'pages'
    docs_folder = 'pages'
    port = '8080'
    not_found_text = 'Page Not Found'
    main_title = 'Block note'

    def __init__(self):
        if function.check_found_file(self.config_file_name):
            config = ConfigParser.RawConfigParser()
            config.read(self.config_file_name, encoding='utf-8')
            self.start_page = config.get('app_setting', 'start_page')
            self.side_bar = config.get('app_setting', 'side_bar')
            self.pages_folder = config.get('app_setting', 'pages_folder')
            self.port = config.getint('app_setting', 'port')
            self.not_found_text = config.get('app_setting', 'not_found_text')
            self.main_title = config.get('app_setting', 'main_title')
            self.docs_folder = config.get('app_setting', 'docs_folder')