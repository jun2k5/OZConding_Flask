from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_smorest import Api
from user_routes import create_user_blueprint

import dotenv
import os


app = Flask(__name__)

dotenv.load_dotenv()
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

# MYSQL 연동 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = 'oz'

mysql = MySQL(app)


#API 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

#blueprint 설정 및 등록
user_blp = create_user_blueprint(mysql)
api.register_blueprint(user_blp)


@app.route("/user_interface")
def user_interface():
    return render_template("users.html")



if __name__ == "__main__":
    app.run(debug=True)


