#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core import reqparse as rp
from core import report as Report

class Trading:
    def __init__(self):
        self.report = Report.Report()

    def createOrder(self, type=None, amount=None, price=None, market=None):
        if type and amount and price and market:
            if amount <= '0.0001':
                self.report.error(content="Amount has to be larger than 0.")
            if price <= '0.01':
                self.report.error(content="Price has to be larger than 0.")

            obj = {
                'market': market,
                'amount': str(amount),
                'price': str(price),
                'type': type
            }
            self.report.notice(content="Placing order: " + str(obj))
            rp.Parse(url='/orders', data=obj, type='post', auth='true')
        else:
            self.report.error(content="Missing critical information, e.g: order type, amount or price")

    def cancelOrder(self, market=None):
        if market:
            self.report.notice(content="Cancelling all orders at " + market)
            return rp.Parse(url='/orders/' + market , type='delete', auth='true')
            pass
        else:
            self.report.notice(content="Cancelling all orders.")
            return rp.Parse(url='/orders', type='delete', auth='true')
        pass
    

    def orderList(self, market=None):
        if market:
            return rp.Parse(url='/orders/' + market, type='get', auth='true')
        else:
            return rp.Parse(url='/orders/', type='get', auth='true')
    

    def history(self, market=None):
        if market:
            return rp.Parse(url='/orders/' + market + '/history', type='get', auth='true')
        else:
            return rp.Parse(url='/orders/history', type='get', auth='true')



