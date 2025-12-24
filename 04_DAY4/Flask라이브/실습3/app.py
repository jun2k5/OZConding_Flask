from flask import Flask
from flask_sock import Sock
import time
import threading

app = Flask(__name__)
sock = Sock(app)

connections = []

@sock.route('/ws')
def websocket(ws):
    connections.append(ws)
    while True:
        data = ws.receive()
        if data is None:
            break
    connections.remove(ws)

def background_job():
    while True:
        time.sleep(5)
        for ws in list(connections):
            ws.send("알림 전송")




threading.Thread(target=background_job, daemon=True).start()



if __name__ == "__main__":
    app.run(debug=True)



