from flask import Blueprint, jsonify, request
from .models import SessionLocal, Todo

todo_blp = Blueprint("todo", __name__)

#READ
#READ 전체
@todo_blp.route("/todos", methods=['GET'])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task" : t.task} for t in todos])

#READ 특정
@todo_blp.route("/todos/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
#    task = todos.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"id":todo.id, "task": todo.task})


#WRITE
@todo_blp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    db = SessionLocal()
    todo = Todo(task=data["task"])
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()

    return jsonify({"id" : todo.id, "task" : todo.task}), 201

#PUT
@todo_blp.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()

    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error" : "Todo not found"}), 404
    todo.task = data["task"]
    db.commit()
    db.refresh(todo)
    db.close()

    return jsonify({"id" : todo.id, "task" : todo.task})


@todo_blp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)

    if not todo:
        db.close()
        return jsonify({"error" : "Todo not found"}), 404

    db.delete(todo)
    db.commit()
    db.close()

    return jsonify({"delete" : todo_id})