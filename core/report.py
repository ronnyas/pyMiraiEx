#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core import conf as Config
from datetime import date

class Report:
    def __init__(self):
        if hasattr(Config, 'logdefault'):
            self.logdefault = Config.logdefault
        else:
            self.logdefault = 1

        if self.logdefault == 0:
            return

        if hasattr(Config, 'logfile'):
            self.logfile = Config.logfile
        else:
            self.logfile = 'log.txt'

    def error(self, content=None):
        if content:
            self.log(content="Error: " + content)

        raise SystemExit

    def notice(self, content=None):
        if content:
            self.log(content=content)


    def log(self, content=None):
        from datetime import datetime

        time = datetime.now().strftime('%d. %b %Y %H:%M:%S')
        content = time + ' | ' + content

        if self.logdefault >= 2:
            with open(self.logfile, "a") as file:
                file.write(content + "\n")
        
        if self.logdefault == 1 or self.logdefault == 3:
            print(content)

