"""
Contract tests for todo operations based on operations.yaml.
"""

from src.services.todo_manager import TodoManager
from src.cli.main import TodoCLI
from src.lib.utils import parse_command, format_todo_item, validate_todo_description, is_valid_id


class TestTodoOperationsContract:
    """Contract tests for todo operations."""

    def test_add_todo_contract(self):
        """Test add todo operation contract."""
        manager = TodoManager()

        # Add a todo
        todo_item = manager.add_todo("Test description")

        # Verify the todo was added with correct properties
        assert todo_item.id == 1
        assert todo_item.description == "Test description"
        assert todo_item.completed is False

        # Verify it can be retrieved
        retrieved = manager.get_todo(1)
        assert retrieved is not None
        assert retrieved.id == 1
        assert retrieved.description == "Test description"

    def test_add_todo_empty_description_contract(self):
        """Test add todo contract for empty description error case."""
        manager = TodoManager()

        # Attempt to add todo with empty description should raise ValueError
        try:
            manager.add_todo("")
            assert False, "Expected ValueError for empty description"
        except ValueError as e:
            assert "Description cannot be empty" in str(e)

    def test_view_todos_contract(self):
        """Test view todos operation contract."""
        manager = TodoManager()

        # Add some todos
        manager.add_todo("First task")
        manager.add_todo("Second task")

        # Get all todos
        todos = manager.list_todos()

        # Verify the correct number of todos
        assert len(todos) == 2

        # Verify the todos have correct properties
        descriptions = [todo.description for todo in todos]
        assert "First task" in descriptions
        assert "Second task" in descriptions

    def test_update_todo_contract(self):
        """Test update todo operation contract."""
        manager = TodoManager()

        # Add a todo
        original_item = manager.add_todo("Original description")

        # Update the todo
        success = manager.update_todo(original_item.id, "Updated description")

        # Verify update was successful
        assert success is True

        # Verify the todo was updated
        updated_item = manager.get_todo(original_item.id)
        assert updated_item is not None
        assert updated_item.description == "Updated description"

    def test_update_todo_invalid_id_contract(self):
        """Test update todo contract for invalid ID error case."""
        manager = TodoManager()

        # Try to update a non-existent todo
        success = manager.update_todo(999, "Updated description")

        # Should return False
        assert success is False

    def test_update_todo_empty_description_contract(self):
        """Test update todo contract for empty description error case."""
        manager = TodoManager()

        # Add a todo
        item = manager.add_todo("Original description")

        # Try to update with empty description should raise ValueError
        try:
            manager.update_todo(item.id, "")
            assert False, "Expected ValueError for empty description"
        except ValueError as e:
            assert "Description cannot be empty" in str(e)

    def test_mark_complete_contract(self):
        """Test mark complete operation contract."""
        manager = TodoManager()

        # Add a todo
        item = manager.add_todo("Test task")

        # Mark it as complete
        success = manager.mark_complete(item.id)

        # Verify the operation was successful
        assert success is True

        # Verify the todo is now marked as complete
        completed_item = manager.get_todo(item.id)
        assert completed_item is not None
        assert completed_item.completed is True

    def test_mark_complete_invalid_id_contract(self):
        """Test mark complete contract for invalid ID error case."""
        manager = TodoManager()

        # Try to mark a non-existent todo as complete
        success = manager.mark_complete(999)

        # Should return False
        assert success is False

    def test_delete_todo_contract(self):
        """Test delete todo operation contract."""
        manager = TodoManager()

        # Add a todo
        item = manager.add_todo("Test task")

        # Verify it exists
        assert manager.get_todo(item.id) is not None

        # Delete the todo
        success = manager.delete_todo(item.id)

        # Verify the operation was successful
        assert success is True

        # Verify the todo no longer exists
        assert manager.get_todo(item.id) is None

    def test_delete_todo_invalid_id_contract(self):
        """Test delete todo contract for invalid ID error case."""
        manager = TodoManager()

        # Try to delete a non-existent todo
        success = manager.delete_todo(999)

        # Should return False
        assert success is False


class TestCLIContract:
    """Contract tests for CLI interface."""

    def test_cli_input_validation(self):
        """Test CLI input validation contract."""
        # Test ID validation
        assert is_valid_id("1") is True
        assert is_valid_id("999") is True
        assert is_valid_id("0") is False
        assert is_valid_id("-1") is False
        assert is_valid_id("abc") is False
        assert is_valid_id("") is False

        # Test description validation
        assert validate_todo_description("valid description") is True
        assert validate_todo_description("") is False
        assert validate_todo_description("   ") is False

    def test_cli_command_parsing(self):
        """Test CLI command parsing contract."""
        # Test add command parsing
        command, args = parse_command('add "Buy groceries"')
        assert command == "add"
        assert "Buy groceries" in " ".join(args) or len(args) >= 1

        # Test view command parsing
        command, args = parse_command('view')
        assert command == "view"
        assert len(args) == 0

        # Test update command parsing
        command, args = parse_command('update 1 "Updated description"')
        assert command == "update"
        assert "1" in args or len(args) >= 2

        # Test complete command parsing
        command, args = parse_command('complete 1')
        assert command == "complete"
        assert "1" in args

        # Test delete command parsing
        command, args = parse_command('delete 1')
        assert command == "delete"
        assert "1" in args

    def test_cli_output_formatting(self):
        """Test CLI output formatting contract."""
        from src.models.todo import TodoItem

        # Test incomplete todo formatting
        incomplete_item = TodoItem(id=1, description="Test task", completed=False)
        formatted = format_todo_item(incomplete_item)
        assert "[ ]" in formatted
        assert "1 - Test task" in formatted

        # Test complete todo formatting
        complete_item = TodoItem(id=1, description="Test task", completed=True)
        formatted = format_todo_item(complete_item)
        assert "[X]" in formatted
        assert "1 - Test task" in formatted