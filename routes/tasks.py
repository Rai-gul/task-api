from flask import Blueprint, jsonify, request
from models.task_model import Task
from app import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "done": t.done} for t in tasks])

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new = Task(title=data.get("title"))
    db.session.add(new)
    db.session.commit()
    return jsonify({"id": new.id, "title": new.title, "done": new.done}), 201



@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.done = data.get("done", task.done)

    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "done": task.done})

