from symtable import Symbol
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd

apikey = 'YOURAPIKEY'
secret = 'YOURAPISECRET'
pair='ETHBTC'

client = Client(apikey, secret)

tickers = client.get_all_tickers()

trythis = client.get_ticker(symbol = pair)

print(trythis)

dicte = {}
dicte = trythis

for i in dicte.keys():
    print(i)
