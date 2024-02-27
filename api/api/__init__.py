from flask import Flask, make_response, jsonify
from flask_cors import CORS
from .routes.todos import todos_bp
from api.database import db

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
    db.init_app(app)
    
    app.register_blueprint(todos_bp, url_prefix='/todos')
    
    CORS(app)
    
    return app

app = create_app()
    
    