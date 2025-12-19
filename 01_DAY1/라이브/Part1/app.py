from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Flask!"

#정적 라우팅
@app.route("/login")
def log_in():
    return "로그인 페이지입니다~"

# #동적 라우팅
# @app.route("/user/<name>/<int:age>")
# def greet(name, age):
#     return f"{name}님, {age}살입니다. 환영합니다!"

#Jinja2 템플릿
@app.route("/hello")
def hello():
    return render_template("hello.html", name="은행")

#제어문 바인딩
@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

#반복문 바인딩
@app.route("/fruits")
def fruits():
    fruits = ["사과", "바나나", "딸기", "포도"]
    return render_template("fruits.html", fruits=fruits)


if __name__ == "__main__":
    app.run(debug=True)






