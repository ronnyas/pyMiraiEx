#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core import reqparse as rp

class MarketInformation:
    def marketData(self, market=None, type=None):
        if not market and not type:
            return rp.Parse(url='/markets', type='get')
        elif market:
            if not type:
                return rp.Parse(url='/markets/' + market, type='get')
            else:
                return rp.Parse(url='/markets/' + market + '/' + type, type='get')
    
    def availableTickers(self):
        fetchTickers = self.marketData('tickers')
        tickers = []

        for ticker in fetchTickers:
            tickers.append(ticker['market'])

        return tickers

    def history(self, ticker):
        return self.marketData(ticker, 'history')

    def depth(self, ticker):
        return self.marketData(ticker, 'depth')

    def ticker(self, ticker):
        return self.marketData(ticker, 'ticker')
            
    def tickers(self):
        return self.marketData('tickers')