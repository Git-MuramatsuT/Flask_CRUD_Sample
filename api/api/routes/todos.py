from flask import Blueprint, request, make_response, jsonify
from api.models import Todos, TodosSchema 
import json

todos_bp = Blueprint('todos', __name__)

@todos_bp.route('/', methods=['GET'])
def get_todos_list():
    todos = Todos.get_all()
    todos_schema = TodosSchema(many=True)
    
    return make_response(jsonify({
        'code': 200,
        'todos': todos_schema.dump(todos)
    }))
    

@todos_bp.route('/', methods=['POST'])
def add_todo():
    json_data = json.dumps(request.json)
    todo_data = json.loads(json_data)
    
    todo = Todos.register(todo_data)
    todo_schema = TodosSchema(many=True)
    
    return make_response(jsonify({
        'code': 200,
        'todo': todo
    }))
    
@todos_bp.route('/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todos.get(id)
    todo_schema = TodosSchema(many=False)
    
    return make_response(jsonify({
        'code': 200,
        'todo': todo_schema.dump(todo)
    }))    
    
    

@todos_bp.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    json_data = json.dumps(request.json)
    todo_data = json.loads(json_data)
    
    Todos.update(id, todo_data)
    
    return make_response(jsonify({
       'code': 200, 
    }))
    
@todos_bp.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    Todos.delete(id)
    return make_response(jsonify({
       'code': 204, 
    }))