from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd

apikey = 'YOURAPIKEY'
secret = 'YOURAPISECRET'
pair='XBTZAR'

client = Client(apikey, secret)

tickers = client.get_all_tickers()

trythis = client.get_ticker()

print(trythis)