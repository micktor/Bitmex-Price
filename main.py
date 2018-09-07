import websocket
import os
import json
import datetime
import time
import threading
import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# app = QApplication(sys.argv)
#
# w = QWidget()
#
# w.setWindowTitle('Simple')
# w.show()
#
# sys.exit(app.exec_())

ws = websocket.create_connection("wss://ws-feed.pro.coinbase.com/")
ws.send('{     "type": "subscribe",     "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}] }')
resultt = ws.recv()
print(resultt)
resultt = ws.recv()

ws2 = websocket.create_connection("wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD")
resultt = ws2.recv()
print(resultt)
resultt = ws2.recv()

ws3 = websocket.create_connection("wss://stream.binance.com:9443/ws/btcusdt@trade")
resultt = ws3.recv()
print(resultt)
resultt = ws3.recv()




def binance():
    while True:
        result3 = ws3.recv()
        obj3 = json.loads(result3)
        price3 = obj3["p"]
        #time = obj["time"]
        print("binance " + str(price3))


def coinbase():

    while True:
        result1 = ws.recv()
        obj = json.loads(result1)
        price = obj["price"]
        #time = obj["time"]
        print("coinbase " + str(price))


def bitmex():
    while True:
        result2 = ws2.recv()
        obj2 = json.loads(result2)
        price2 = obj2["data"][0]["price"]
        #time = obj2["data"][0]["timestamp"]
        print("bitmex " + str(price2))


t = threading.Thread(name='coinbase', target=coinbase)
w = threading.Thread(name='bitmex', target=bitmex)
v = threading.Thread(name='binance', target=binance)



t.start()
w.start()
v.start()


