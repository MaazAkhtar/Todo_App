"""
Unit tests for TodoItem model in src/models/todo.py.
"""

import pytest
from src.models.todo import TodoItem, TodoList


class TestTodoItem:
    """Test cases for the TodoItem model."""

    def test_todo_item_creation(self):
        """Test creating a TodoItem with valid parameters."""
        item = TodoItem(id=1, description="Test description")
        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is False

    def test_todo_item_creation_with_completed(self):
        """Test creating a TodoItem with completed status."""
        item = TodoItem(id=1, description="Test description", completed=True)
        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is True

    def test_todo_item_validation_id_positive(self):
        """Test that ID must be a positive integer."""
        # Valid case
        item = TodoItem(id=1, description="Test")
        assert item.id == 1

        # Invalid cases should raise ValueError
        with pytest.raises(ValueError):
            TodoItem(id=0, description="Test")

        with pytest.raises(ValueError):
            TodoItem(id=-1, description="Test")

        with pytest.raises(ValueError):
            TodoItem(id="invalid", description="Test")

    def test_todo_item_validation_description_non_empty(self):
        """Test that description must be non-empty."""
        # Valid case
        item = TodoItem(id=1, description="Test description")
        assert item.description == "Test description"

        # Invalid cases should raise ValueError
        with pytest.raises(ValueError):
            TodoItem(id=1, description="")

        with pytest.raises(ValueError):
            TodoItem(id=1, description=None)

    def test_todo_item_validation_completed_boolean(self):
        """Test that completed must be a boolean."""
        # Valid cases
        item1 = TodoItem(id=1, description="Test", completed=True)
        item2 = TodoItem(id=2, description="Test", completed=False)
        assert item1.completed is True
        assert item2.completed is False

        # Invalid case should raise ValueError
        with pytest.raises(ValueError):
            TodoItem(id=1, description="Test", completed="not_boolean")


class TestTodoList:
    """Test cases for the TodoList container."""

    def test_todo_list_initialization(self):
        """Test that TodoList initializes correctly."""
        todo_list = TodoList()
        assert len(todo_list.items) == 0
        assert todo_list.next_id == 1

    def test_add_item(self):
        """Test adding items to the list."""
        todo_list = TodoList()

        item = todo_list.add_item("Test description")
        assert item.id == 1
        assert item.description == "Test description"
        assert item.completed is False
        assert len(todo_list.items) == 1
        assert 1 in todo_list.items
        assert todo_list.next_id == 2

    def test_add_item_empty_description(self):
        """Test that adding an item with empty description raises an error."""
        todo_list = TodoList()

        with pytest.raises(ValueError):
            todo_list.add_item("")

    def test_get_item(self):
        """Test retrieving an item by ID."""
        todo_list = TodoList()
        item = todo_list.add_item("Test description")

        retrieved_item = todo_list.get_item(1)
        assert retrieved_item is not None
        assert retrieved_item.id == 1
        assert retrieved_item.description == "Test description"

    def test_get_item_not_found(self):
        """Test retrieving a non-existent item."""
        todo_list = TodoList()

        retrieved_item = todo_list.get_item(999)
        assert retrieved_item is None

    def test_update_item(self):
        """Test updating an item's description."""
        todo_list = TodoList()
        item = todo_list.add_item("Original description")

        success = todo_list.update_item(1, "Updated description")
        assert success is True
        assert todo_list.items[1].description == "Updated description"

    def test_update_item_not_found(self):
        """Test updating a non-existent item."""
        todo_list = TodoList()

        success = todo_list.update_item(999, "Updated description")
        assert success is False

    def test_update_item_empty_description(self):
        """Test updating an item with empty description raises an error."""
        todo_list = TodoList()
        item = todo_list.add_item("Original description")

        with pytest.raises(ValueError):
            todo_list.update_item(1, "")

    def test_mark_complete(self):
        """Test marking an item as complete."""
        todo_list = TodoList()
        item = todo_list.add_item("Test description")

        success = todo_list.mark_complete(1)
        assert success is True
        assert todo_list.items[1].completed is True

    def test_mark_complete_not_found(self):
        """Test marking a non-existent item as complete."""
        todo_list = TodoList()

        success = todo_list.mark_complete(999)
        assert success is False

    def test_delete_item(self):
        """Test deleting an item."""
        todo_list = TodoList()
        item = todo_list.add_item("Test description")

        success = todo_list.delete_item(1)
        assert success is True
        assert len(todo_list.items) == 0
        assert 1 not in todo_list.items

    def test_delete_item_not_found(self):
        """Test deleting a non-existent item."""
        todo_list = TodoList()

        success = todo_list.delete_item(999)
        assert success is False

    def test_list_all(self):
        """Test listing all items."""
        todo_list = TodoList()
        item1 = todo_list.add_item("Description 1")
        item2 = todo_list.add_item("Description 2")

        all_items = todo_list.list_all()
        assert len(all_items) == 2
        descriptions = [item.description for item in all_items]
        assert "Description 1" in descriptions
        assert "Description 2" in descriptions

    def test_get_next_id(self):
        """Test getting the next available ID."""
        todo_list = TodoList()
        assert todo_list.get_next_id() == 1

        item = todo_list.add_item("Test description")
        assert todo_list.get_next_id() == 2