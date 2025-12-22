from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the requirement")

    return "Success!"

if __name__ == "__main__":
    app.run(debug=True)