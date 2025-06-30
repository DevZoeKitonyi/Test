# 🚀 Advanced Todo Web Application

A modern, responsive todo list application built with Flask, HTMX, and Tailwind CSS.

![Todo App Screenshot](screenshot.png)

## ✨ Features

- **CRUD Operations**: Create, Read, Update, Delete todos
- **Priority Levels**: High/Medium/Low priority indicators
- **Interactive UI**: HTMX for AJAX without JavaScript
- **Responsive Design**: Works on mobile and desktop
- **Persistence**: SQLite database storage
- **Modern Styling**: Tailwind CSS with custom animations

## 🛠️ Technologies Used

- **Backend**: Python + Flask
- **Frontend**: HTMX + Tailwind CSS
- **Database**: SQLAlchemy + SQLite
- **Templating**: Jinja2

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-webapp.git
   cd todo-webapp

2.Create and activate virtual environment:
   python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate


3.Install dependencies:
pip install -r requirements.txt


4.Initialize database:
python -c "from app import app, db; with app.app_context(): db.create_all()"


Running the Application
python app.py


📂 Project Structure

todo-webapp/
├── app.py              # Flask application
├── models.py           # Database models
├── requirements.txt    # Dependencies
├── static/
│   └── styles.css      # Custom CSS
└── templates/
    ├── base.html       # Base template
    ├── index.html      # Main view
    ├── todo_item.html  # Single todo component
    └── todo_list.html  # Todo list component


    
🌐 API Endpoints
Method	Endpoint	Description
GET	/	Render main page
POST	/todos	Create new todo
PUT	/todos/<id>/toggle	Toggle completion status
DELETE	/todos/<id>	Delete a todo
DELETE	/todos/clear-completed	Clear all completed todos

🛠️ Development

Running Tests
python -m pytest

Code Formatting

bash
python -m black .
Creating Requirements

bash
pip freeze > requirements.txt
