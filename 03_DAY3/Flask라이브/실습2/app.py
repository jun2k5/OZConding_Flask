from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os




app=Flask(__name__)

# DB 설정

BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True) # instance 폴더가 없으면 생성

DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR, 'todos.db')}" 
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread":False})



Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo id={self.id} task='{self.task}'>"


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)


#READ
#READ 전체
@app.route("/todos", methods=['GET'])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task" : t.task} for t in todos])

#READ 특정
@app.route("/todos/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
#    task = todos.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"id":todo.id, "task": todo.task})


#WRITE
@app.route("/todos", methods=["POST"])
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
@app.route("/todos/<int:todo_id>", methods=["PUT"])
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


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
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


if __name__ == "__main__":
    app.run(debug=True)