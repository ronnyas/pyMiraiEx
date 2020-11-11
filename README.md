pyMiraiEx
===

Lightweight python SDK for the MiraiEx API (v2)

## Example usage
```python
from miraiex import pyMiraiEx

miraiex = pyMiraiEx()

# check if I have any active orders
if not miraiex.trade.orderList('BTCNOK'):
    # get latest 'ask' for BTCNOK
    currentAsk = miraiex.market.ticker('BTCNOK')['ask']

    if currentAsk < 150000:
        # place order if current price is within range
        miraiex.trade.createOrder(type='bid', market='BTCNOK',price=str(currentAsk),amount='0.005')
        print("Order placed.")
```

## How to use

See core/conf.py to configure how to output responses.

### Public API
```python
#Returns dict with the current time from API server
    miraiex.getTime()

#Returns list of dicts with the latest orders at chosen market
    miraiex.market.history('BTCNOK')

#Returns dict with lists of current bids/asks 
    miraiex.market.depth('BTCNOK')

#Returns dict with top bid, ask and spread
    miraiex.market.ticker('BTCNOK')

#Returns list with dicts of top bid, ask and spread for all available markets
    miraiex.market.tickers()

#Returns list of all available markets.
    miraiex.market.availableTickers()
```

### Private API
```python
#There will require accessKey (see core/conf.py)
    miraiex.acc.history(data='deposit')
    miraiex.acc.history(data='orders')
    miraiex.acc.history(data='orders', market='BTCNOK')

    miraiex.acc.history(data='trades')
    miraiex.acc.history(data='trades', year='2020')
    miraiex.acc.history(data='trades', year='2020', month='02')

    miraiex.acc.history(data='transactions')
    miraiex.acc.history(data='transactions', year='2020')
    miraiex.acc.history(data='transactions', year='2020', month='02')

#Returns dict of all addresses owned by the account
    miraiex.acc.addresses()

#Send an order to market. Type: 'bid' or 'ask'.
#Minimum price: 0.01, minimum amount: 0.0001
    miraiex.trade.createOrder(type='bid', market='BTCNOK', price='0.0123', amount='1')

#Cancel all orders
    miraiex.trade.cancelOrder()

#Cancel all orders at one market only, e.g BTCNOK
    miraiex.trade.cancelOrder(market='BTCNOK')

#Returns list with dict of all active orders
    miraiex.trade.orderList()

#Returns list with dict of all active orders at one market only, e.g BTCNOK
    miraiex.trade.orderList(market='BTCNOK')
```

