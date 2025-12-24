from flask_sock import Sock
from flask import Flask, render_template


app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("sentiment.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        data = ws.receive()        
        if data is None:
            break

        #감정 분석
        pos = ["happy", "good", "love", "lucky", "wow"]
        nag = ["bad", "hate", "sad", "angry"]
        # sentiment = "So So"

        if any(word in data.lower() for word in pos):
            sentiment="😊Positive"
        elif any(word in data.lower() for word in nag):
            sentiment="😭Nagative"
        else:
            sentiment = "So So"
        # for word in pos:
        #     if word in data:
        #         sentiment="😊Positive"


        # for word in nag:
        #     if word in data:
        #         sentiment="😭Nagative"

        ws.send(sentiment)


if __name__ == "__main__":
    app.run(debug=True)









