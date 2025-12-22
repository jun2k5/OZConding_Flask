# REST API 
# JSON
# {"key" : "value"},
# flask에서 JSON 반환 방벙
# 1. return {"message" : "Hello, OZ BE!"}
# 2. return jsonify(message="Hello, OZ BE!")
#
#

from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

swagger = Swagger(app)

@app.route("/user/<name>")
def user(name):
    return jsonify(message=f"{name}님, BE 캠프에 오신 걸 환영합니다!")

if __name__ == "__main__":
    app.run(debug=True)








