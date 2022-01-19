from luno_python.client import Client
import time
import datetime

def test():
    period = 2
    pair='XBTZAR'
    
    con = Client(api_key_id='bm5srszevbqv4', api_key_secret='HfHlxYlxOY3rhHUuw-szHKH84592y6uYIuTq1rh5VVg')
    

    while True:
        try:
            ticker = con.get_ticker(pair)
            lastPairPrice = ticker['ask']
            printDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #print(res)
            gap = float(ticker['ask']) - float(ticker['bid'])
            print("{} {} - ASK: {} \tBID: {} \tGAP: {}" .format(printDate, pair, lastPairPrice[:-2], ticker['bid'], str(gap)[:-2]))
        except Exception as e:
            print(e)
        
        
        time.sleep(period)


    


w = 1
test()

