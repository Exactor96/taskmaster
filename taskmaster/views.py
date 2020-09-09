from datetime import datetime

import pymongo
from bson import ObjectId
from bson.json_util import dumps
from flask import request, jsonify

from .config import Config
from .validators import task_validation

db = pymongo.MongoClient(Config.MONGODB_URL).taskmanager


def create_task():
    request_json = request.get_json()
    request_json['user'] = 'test'
    if task_validation(request_json):
        task_id = db.tasks.insert_one(request_json).inserted_id
        response_json = {'taskId': str(task_id)}
        return jsonify(response_json)
    else:
        return jsonify({'error': 'error in data occurred'})


def get_task(task_id):
    return dumps({'task': db.tasks.find_one({'_id': ObjectId(task_id)})})


def delete_task(task_id):
    return dumps(
        {'success': True,
         'task_count': db.tasks.delete_one({'_id': ObjectId(task_id)}).deleted_count,
         }
    )


def update_task(task_id):
    request_json = request.get_json()
    request_json.pop('taskId')
    request_json.update({'is_updated': True, 'update_datetime': datetime.now()})
    result = db.messages.update_one({'_id': ObjectId(task_id)}, {'$set': request_json})
    return jsonify({'success': True, 'task_count': result.modified_count})


def tasks_list():
    data = request.values
    if 'datetime' in data:
        return dumps(
            {'tasks': db.tasks.find({'datetime': data['datetime']})}
        )
    else:
        return jsonify({'error': 'datetime is not found'})


def test():
    return 'test'
