# coding=utf-8

import ConfigParser
import function


class ConfigProvider:
    config_file_name = 'config.ini'
    start_page = 'start'
    side_bar = 'sidebar'
    pages_folder = 'pages'
    port = '8080'
    not_found_text = 'Page Not Found'
    main_title = u'Записная книжка'

    def __init__(self):
        # Если существует файл с конфигурацией
        if function.check_found_file(self.config_file_name):
            config = ConfigParser.RawConfigParser()
            config.read(self.config_file_name)
            # Перезапись значений по умолчанию
            self.start_page = config.get('app_setting', 'start_page').decode('utf8')
            self.side_bar = config.get('app_setting', 'side_bar').decode('utf8')
            self.pages_folder = config.get('app_setting', 'pages_folder').decode('utf8')
            self.port = config.getint('app_setting', 'port')
            self.not_found_text = config.get('app_setting', 'not_found_text').decode('utf8')
            self.main_title = config.get('app_setting', 'main_title').decode('utf8')