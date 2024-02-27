from api.database import db, ma
from datetime import datetime

class Todos(db.Model):
    __tablename__ = 'todo'
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    deadline = db.Column(db.Date)
    
    def get_all():
        todo_list = db.session.query(Todos).all()
        
        return todo_list
    
    def register(todo):
        record = Todos(
            task = todo['task'],
            deadline = datetime.strptime(todo['deadline'], '%Y-%m-%d')
        )
        
        db.session.add(record)
        db.session.commit()
        
        return todo
    
    def get(id):
        todo = db.session.query(Todos).get(id)
        return todo
    
    def update(id, todo):
        todo_a = db.session.query(Todos).get(id)
        
        todo_a.task = todo['task']
        todo_a.deadline = datetime.strptime(todo['deadline'], '%Y-%m-%d')
        
        db.session.commit()
        
    def delete(id):
        todo_a = db.session.query(Todos).get(id)
        db.session.delete(todo_a)
        db.session.commit()    
        
    
class TodosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todos
        fields = ('id', 'task', 'deadline')