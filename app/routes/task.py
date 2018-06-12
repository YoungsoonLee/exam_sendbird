from flask import Blueprint,jsonify,request
from app import db
from app.models.task import TaskModel
from app.models.category import CategoryModel
from sqlalchemy.exc import IntegrityError

task = Blueprint('task', 'task', url_prefix='/api/tasks')

@task.route('', methods=['GET'])
def get_tasks():
    try:
        tasks = []
        tasks_query = TaskModel.query.filter()

        print(tasks_query)

        for task in tasks_query:
            tasks.append(serialize_task(task))

        return jsonify(tasks) 

    except IntegrityError as e:
        print(e)

@task.route('/<id>', methods=['GET'])
def get_task(id):
    # validation
    try:
        task = TaskModel.query.filter(TaskModel.id == id).first()
        if not task:
            err = {
                "code": 403, 
                "message": "not exists task id"
            }
            return jsonify(err)
        else:
            return jsonify(serialize_task(task))
    except IntegrityError as e:
        err = {
            "code": 404,
            "message": "not exists task id"
        }
        return jsonify(err)

def serialize_task(task):
    return {
        'id': task.id,
        'title': task.title,
        'created_at': task.created_at,
        'category_id': task.category_id,
        'category_title': task.category_title
    }