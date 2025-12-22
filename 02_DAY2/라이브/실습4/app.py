from flask import Flask, jsonify, request

app=Flask(__name__)

todos = {
    1: "공부하기",
    2: "청소하기"

}

#READ
#READ 전체
@app.route("/todos", methods=['GET'])
def get_todos():
    return jsonify(todos)

#READ 특정
@app.route("/todos/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({todo_id : task})


#WRITE
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data["task"]
    return jsonify({new_id : todos[new_id]}), 201

#PUT
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error" : "Todo not found"}), 404
    data = request.get_json()
    todos[todo_id] = data["task"]
    return jsonify({todo_id : todos[todo_id]})

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error" : "Todo not found"}), 404
    deleted = todos.pop(todo_id)
    return jsonify({"delete" : deleted})




if __name__ == "__main__":
    app.run(debug=True)