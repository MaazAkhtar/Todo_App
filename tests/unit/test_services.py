"""
Unit tests for todo service functionality in src/services/todo_manager.py.
"""

import pytest
from src.services.todo_manager import TodoManager


class TestTodoManager:
    """Test cases for the TodoManager service."""

    def test_add_todo(self):
        """Test adding a new todo item."""
        manager = TodoManager()

        item = manager.add_todo("Test description")

        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is False
        assert len(manager.list_todos()) == 1

    def test_add_todo_empty_description(self):
        """Test that adding a todo with empty description raises an error."""
        manager = TodoManager()

        with pytest.raises(ValueError):
            manager.add_todo("")

    def test_add_todo_whitespace_description(self):
        """Test that adding a todo with only whitespace description raises an error."""
        manager = TodoManager()

        with pytest.raises(ValueError):
            manager.add_todo("   ")

    def test_add_multiple_todos(self):
        """Test adding multiple todo items with unique IDs."""
        manager = TodoManager()

        item1 = manager.add_todo("First description")
        item2 = manager.add_todo("Second description")
        item3 = manager.add_todo("Third description")

        assert item1.id == 1
        assert item2.id == 2
        assert item3.id == 3

        todos = manager.list_todos()
        assert len(todos) == 3

        descriptions = [todo.description for todo in todos]
        assert "First description" in descriptions
        assert "Second description" in descriptions
        assert "Third description" in descriptions

    def test_list_todos_empty(self):
        """Test listing todos when the list is empty."""
        manager = TodoManager()

        todos = manager.list_todos()

        assert len(todos) == 0

    def test_list_todos_with_items(self):
        """Test listing todos when the list has items."""
        manager = TodoManager()

        manager.add_todo("First description")
        manager.add_todo("Second description")

        todos = manager.list_todos()

        assert len(todos) == 2
        descriptions = [todo.description for todo in todos]
        assert "First description" in descriptions
        assert "Second description" in descriptions

    def test_get_todo(self):
        """Test getting a specific todo by ID."""
        manager = TodoManager()

        added_item = manager.add_todo("Test description")
        retrieved_item = manager.get_todo(added_item.id)

        assert retrieved_item is not None
        assert retrieved_item.id == added_item.id
        assert retrieved_item.description == added_item.description
        assert retrieved_item.completed == added_item.completed

    def test_get_todo_not_found(self):
        """Test getting a non-existent todo."""
        manager = TodoManager()

        retrieved_item = manager.get_todo(999)

        assert retrieved_item is None

    def test_update_todo(self):
        """Test updating a todo's description."""
        manager = TodoManager()

        item = manager.add_todo("Original description")
        success = manager.update_todo(item.id, "Updated description")

        assert success is True

        updated_item = manager.get_todo(item.id)
        assert updated_item.description == "Updated description"

    def test_update_todo_empty_description(self):
        """Test that updating a todo with empty description raises an error."""
        manager = TodoManager()

        item = manager.add_todo("Original description")

        with pytest.raises(ValueError):
            manager.update_todo(item.id, "")

    def test_update_todo_not_found(self):
        """Test updating a non-existent todo."""
        manager = TodoManager()

        success = manager.update_todo(999, "Updated description")

        assert success is False

    def test_mark_complete(self):
        """Test marking a todo as complete."""
        manager = TodoManager()

        item = manager.add_todo("Test description")
        assert item.completed is False

        success = manager.mark_complete(item.id)

        assert success is True

        completed_item = manager.get_todo(item.id)
        assert completed_item.completed is True

    def test_mark_complete_not_found(self):
        """Test marking a non-existent todo as complete."""
        manager = TodoManager()

        success = manager.mark_complete(999)

        assert success is False

    def test_delete_todo(self):
        """Test deleting a todo."""
        manager = TodoManager()

        item = manager.add_todo("Test description")
        initial_count = len(manager.list_todos())

        success = manager.delete_todo(item.id)

        assert success is True
        assert len(manager.list_todos()) == initial_count - 1

        deleted_item = manager.get_todo(item.id)
        assert deleted_item is None

    def test_delete_todo_not_found(self):
        """Test deleting a non-existent todo."""
        manager = TodoManager()

        success = manager.delete_todo(999)

        assert success is False

    def test_get_next_id(self):
        """Test getting the next available ID."""
        manager = TodoManager()

        assert manager.get_next_id() == 1

        manager.add_todo("Test description")
        assert manager.get_next_id() == 2

        manager.add_todo("Another description")
        assert manager.get_next_id() == 3