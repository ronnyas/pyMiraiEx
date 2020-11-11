#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core import conf as Config
from core import report as Report

class pyMiraiEx:
    def __init__(self):
        self.report = Report.Report()

        if hasattr(Config, 'api_version') and hasattr(Config, 'api_url'):
            self.api_version = Config.api_version
            self.api_url = Config.api_url + Config.api_version

            from core import reqparse as rp
            from core import market
            from core import useraccount as User
            from core import trading

            self.acc = User.Account()
            self.trade = trading.Trading()
            self.market = market.MarketInformation()
        else:
            self.report.error(content='Missing API URL and/or version number. Check core/config.py')

    def getTime(self):
        return rp.Parse(url='/time', type='get')


