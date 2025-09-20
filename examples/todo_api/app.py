"""
Todo List API - GitHub Copilot Training Example

This is a simple Flask API for managing todo items.
Use this as practice for writing descriptive comments and function names
that help GitHub Copilot generate better API code.
"""

from flask import Flask, request, jsonify
from datetime import datetime
from typing import List, Dict, Optional

app = Flask(__name__)

# In-memory storage for demo purposes (use a real database in production)
todos = []
next_id = 1


class TodoItem:
    """Represents a todo item with all necessary properties."""
    
    def __init__(self, title: str, description: str = "", completed: bool = False):
        global next_id
        self.id = next_id
        next_id += 1
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert todo item to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def update_from_dict(self, data: Dict) -> None:
        """Update todo item properties from dictionary."""
        if 'title' in data:
            self.title = data['title']
        if 'description' in data:
            self.description = data['description']
        if 'completed' in data:
            self.completed = data['completed']
        self.updated_at = datetime.now().isoformat()


def validate_todo_data(data: Dict) -> List[str]:
    """
    Validate todo item data and return list of error messages.
    
    Args:
        data: Dictionary containing todo data
        
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    if not data:
        errors.append("Request body is required")
        return errors
    
    if 'title' not in data or not data['title'].strip():
        errors.append("Title is required and cannot be empty")
    
    if 'title' in data and len(data['title']) > 200:
        errors.append("Title cannot exceed 200 characters")
    
    if 'description' in data and len(data['description']) > 1000:
        errors.append("Description cannot exceed 1000 characters")
    
    if 'completed' in data and not isinstance(data['completed'], bool):
        errors.append("Completed must be a boolean value")
    
    return errors


def find_todo_by_id(todo_id: int) -> Optional[TodoItem]:
    """
    Find a todo item by its ID.
    
    Args:
        todo_id: The ID of the todo to find
        
    Returns:
        TodoItem if found, None otherwise
    """
    return next((todo for todo in todos if todo.id == todo_id), None)


@app.route('/todos', methods=['GET'])
def get_all_todos():
    """
    Get all todo items.
    
    Returns:
        JSON response with list of all todos
    """
    return jsonify([todo.to_dict() for todo in todos])


@app.route('/todos', methods=['POST'])
def create_todo():
    """
    Create a new todo item.
    
    Expected JSON body:
    {
        "title": "Todo title",
        "description": "Optional description",
        "completed": false
    }
    
    Returns:
        JSON response with created todo or error messages
    """
    data = request.get_json()
    errors = validate_todo_data(data)
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    new_todo = TodoItem(
        title=data['title'],
        description=data.get('description', ''),
        completed=data.get('completed', False)
    )
    
    todos.append(new_todo)
    
    return jsonify(new_todo.to_dict()), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id: int):
    """
    Get a specific todo item by ID.
    
    Args:
        todo_id: The ID of the todo to retrieve
        
    Returns:
        JSON response with todo data or 404 if not found
    """
    todo = find_todo_by_id(todo_id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todo.to_dict())


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id: int):
    """
    Update an existing todo item.
    
    Args:
        todo_id: The ID of the todo to update
        
    Expected JSON body (all fields optional):
    {
        "title": "Updated title",
        "description": "Updated description",
        "completed": true
    }
    
    Returns:
        JSON response with updated todo or error messages
    """
    todo = find_todo_by_id(todo_id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    data = request.get_json()
    errors = validate_todo_data(data)
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    todo.update_from_dict(data)
    
    return jsonify(todo.to_dict())


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    """
    Delete a todo item by ID.
    
    Args:
        todo_id: The ID of the todo to delete
        
    Returns:
        JSON response with success message or 404 if not found
    """
    todo = find_todo_by_id(todo_id)
    
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    todos.remove(todo)
    
    return jsonify({'message': 'Todo deleted successfully'})


@app.route('/todos/completed', methods=['GET'])
def get_completed_todos():
    """
    Get all completed todo items.
    
    Returns:
        JSON response with list of completed todos
    """
    completed_todos = [todo for todo in todos if todo.completed]
    return jsonify([todo.to_dict() for todo in completed_todos])


@app.route('/todos/pending', methods=['GET'])
def get_pending_todos():
    """
    Get all pending (not completed) todo items.
    
    Returns:
        JSON response with list of pending todos
    """
    pending_todos = [todo for todo in todos if not todo.completed]
    return jsonify([todo.to_dict() for todo in pending_todos])


@app.errorhandler(400)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(404)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def handle_internal_server_error(error):
    """Handle 500 Internal Server Error."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Add some sample data for testing
    sample_todos = [
        TodoItem("Learn GitHub Copilot", "Practice using Copilot for coding", False),
        TodoItem("Build a Flask API", "Create a RESTful API with Flask", False),
        TodoItem("Write documentation", "Document the API endpoints", True)
    ]
    todos.extend(sample_todos)
    
    print("Starting Todo API server...")
    print("API endpoints available:")
    print("  GET    /todos           - Get all todos")
    print("  POST   /todos           - Create new todo")
    print("  GET    /todos/<id>      - Get specific todo")
    print("  PUT    /todos/<id>      - Update todo")
    print("  DELETE /todos/<id>      - Delete todo")
    print("  GET    /todos/completed - Get completed todos")
    print("  GET    /todos/pending   - Get pending todos")
    
    app.run(debug=True, port=5000)