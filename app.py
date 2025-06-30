from flask import Flask, render_template, request, jsonify
from flask_htmx import HTMX
from models import db, Todo
import os

app = Flask(__name__)
htmx = HTMX(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    todos = Todo.query.order_by(Todo.priority, Todo.created_at).all()
    return render_template('index.html', todos=todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.form
    new_todo = Todo(
        title=data['title'],
        description=data.get('description', ''),
        priority=int(data.get('priority', 2))
    )
    db.session.add(new_todo)
    db.session.commit()
    return render_template('todo_item.html', todo=new_todo)

@app.route('/todos/<int:todo_id>/toggle', methods=['PUT'])
def toggle_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return render_template('todo_item.html', todo=todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return ''

@app.route('/todos/clear-completed', methods=['DELETE'])
def clear_completed():
    Todo.query.filter_by(completed=True).delete()
    db.session.commit()
    todos = Todo.query.all()
    return render_template('todo_list.html', todos=todos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)