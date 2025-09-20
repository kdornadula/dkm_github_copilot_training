# Todo List API Example

A simple RESTful API for managing todo items, built with Python and Flask. This example demonstrates how GitHub Copilot can assist with API development.

## 🎯 Learning Focus

- RESTful API design
- Database model creation
- Route handling
- Error handling and validation
- Testing API endpoints

## 🚀 Setup

```bash
cd examples/todo_api
pip install flask
python app.py
```

## 📡 API Endpoints

- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `GET /todos/<id>` - Get a specific todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

## 💡 Copilot Tips for API Development

1. **Start with clear route definitions**:
   ```python
   @app.route('/todos', methods=['GET'])
   def get_all_todos():
       """Get all todo items from the database"""
   ```

2. **Use descriptive model classes**:
   ```python
   class TodoItem:
       """Represents a todo item with title, description, and completion status"""
   ```

3. **Write clear validation functions**:
   ```python
   def validate_todo_data(data):
       """Validate todo item data before saving to database"""
   ```