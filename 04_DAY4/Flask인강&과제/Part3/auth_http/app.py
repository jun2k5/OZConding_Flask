from flask_httpauth import HTTPBasicAuth, session
from flask import Flask, render_template, redirect

app = Flask(__name__)
auth = HTTPBasicAuth()
app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml에 작성

users = {
    'admin' : 'secret',
    'guest':'pw123'
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

@app.route('/logout')
def logout():
    return "Logged out", 401, {'WWW-Authenticate': 'Basic realm="Logout"'}

@auth.error_handler
def auth_error(status):
    return "Access Denied", status

if __name__ == "__main__":
    app.run(debug=True)