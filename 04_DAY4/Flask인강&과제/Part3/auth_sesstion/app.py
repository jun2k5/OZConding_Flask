from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml에 작성

#admin user
users = {
    'john' : 'pw123',
    'leo' : 'pw123'
}

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) #세션 기간설정


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True #세션 유효기간 활성화
        return redirect('/secret')
    else:
        flash("Invalid username or password")
        return redirect('/')


@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect("/")
    

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)







