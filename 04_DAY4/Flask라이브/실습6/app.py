from flask import Flask, render_template
from flask_sock import Sock
import requests
import time

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("btc.html")


@sock.route("/ws")
def websocket(ws):
    while True:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        result = requests.get(url).json()
        data = f"{result["symbol"]}: {result["price"]} $"
        ws.send(data)
        time.sleep(0.2)



if __name__ == "__main__":
    app.run(debug=True)

















