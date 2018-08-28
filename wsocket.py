import websocket
import os
import json

ws = websocket.create_connection("wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD")

result = ws.recv()
print(result)
result = ws.recv()


while True:
    result = ws.recv()

    obj = json.loads(result)
    os.system('clear')
    obj = obj["data"][0]["price"]

    print(obj)

ws.close()
