from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'database.db'

# データベース接続関数
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # DBの取得結果を辞書型にする
    return conn

# ToDoアイテムの取得
@app.route('/todos', methods=['GET'])
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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todo (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)