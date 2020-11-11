#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core import reqparse as rp
from core import report as Report

class Account():
    def __init__(self):
        self.report = Report.Report()
        pass

    def addresses(self):
        return rp.Parse(url='/deposit/address', type='get', auth='true')


    def history(self, data=None, year=None, month=None, market=None):
        if data: 
            if data == 'deposit':
                return rp.Parse(url='/deposit/history', type='get', auth='true')
                
            if data == 'orders':
                if not market:
                    return rp.Parse(url='/history/orders', type='get', auth='true')
                else:
                    return rp.Parse(url='/history/orders/' + market, type='get', auth='true')
                    
            if data == 'trades' or data == 'transactions':
                if year and month:
                    return rp.Parse(url='/history/' + data + '/' + month + '/' + year, type='get', auth='true')

                elif year:
                    return rp.Parse(url='/history/' + data + '/' + year, type='get', auth='true')

                elif not year and not month:
                    return rp.Parse(url='/history/' + data, type='get', auth='true')
        else:
            self.report.error(content="Missing data type: orders, trades or transactions")
            pass