from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, 'database.db')

# データベース接続関数
def get_db_connection():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row  # DBの取得結果を辞書型にする
    return conn

# ToDoアイテムの取得
@app.route('/todos/', methods=['GET'])
def get_todo_list():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo')
    todo_items = cursor.fetchall()
    conn.close()
    return jsonify({'todos': [dict(item) for item in todo_items]})


# ToDoアイテムの追加
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    deadline = data.get('deadline')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todo (task, deadline) VALUES (?, ?)', (task, deadline))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Todo added successfully'}), 200


@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo WHERE id = ?', (id,))
    todo = cursor.fetchone()
    conn.close()
    return jsonify(dict(todo))


@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    task = data.get('task')
    deadline = data.get('deadline')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE todo SET task = ?, deadline = ? WHERE id = ?', (task, deadline, id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Todo updates successfully'}), 200


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todo WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Todo updates successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)