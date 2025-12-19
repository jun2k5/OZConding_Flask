from flask import Flask, render_template
import random

app = Flask(__name__)

cheers = [
		"할 수 있다!!!! 16기",
		"재미있는 flask 재미있는 프레임워크!",
		"이제 진짜 개발을 해볼까요?!",
		"드디어 배운 재료들로 요리를 시작 할 차례~!!",
		"그래도 아직 어려우니까 방심은 금물입니다",
		"이제부터 재밌어질 시간!!!"
]

@app.route("/")
def cheer():
    message = random.choice(cheers)
    return render_template("cheer.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)