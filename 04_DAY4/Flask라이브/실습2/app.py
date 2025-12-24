from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        print(f"받은 메시지: {data}")
        ws.send(f"Echo: {data}")


if __name__ == "__main__":
    app.run(debug=True)



