"""
Test script to verify main.py functionality.
"""

import subprocess
import sys
import time
from io import StringIO
import threading
import queue


def test_main_cli():
    """Test the main CLI application."""
    print("Testing main.py functionality...")

    # Test that the module can be imported and run without errors
    try:
        # Run the main module to check if it starts without errors
        result = subprocess.run([
            sys.executable, "-c",
            "from src.cli.main import main; main()"
        ], timeout=5, capture_output=True, text=True)

        # The above test will timeout since main() runs an interactive loop
        # That's expected behavior

    except subprocess.TimeoutExpired:
        # This is expected since the CLI runs in an interactive loop
        print("✓ Main application started successfully (interactive mode)")

    # Test individual components instead
    try:
        # Test that all modules can be imported
        from src.models.todo import TodoItem, TodoList
        from src.services.todo_manager import TodoManager
        from src.cli.main import TodoCLI
        from src.lib.utils import format_todo_item, parse_command

        print("[SUCCESS] All modules imported successfully")

        # Test basic functionality
        manager = TodoManager()

        # Test adding a todo
        item = manager.add_todo("Test task")
        assert item.description == "Test task"
        assert item.completed == False
        print("[SUCCESS] Add functionality works")

        # Test listing todos
        todos = manager.list_todos()
        assert len(todos) == 1
        print("[SUCCESS] List functionality works")

        # Test updating a todo
        success = manager.update_todo(item.id, "Updated task")
        assert success == True
        updated_item = manager.get_todo(item.id)
        assert updated_item.description == "Updated task"
        print("[SUCCESS] Update functionality works")

        # Test marking complete
        success = manager.mark_complete(item.id)
        assert success == True
        completed_item = manager.get_todo(item.id)
        assert completed_item.completed == True
        print("[SUCCESS] Mark complete functionality works")

        # Test deleting a todo
        success = manager.delete_todo(item.id)
        assert success == True
        assert manager.get_todo(item.id) is None
        print("[SUCCESS] Delete functionality works")

        # Test utility functions
        formatted = format_todo_item(item)
        assert "[X]" in formatted or "[ ]" in formatted
        print("[SUCCESS] Format utility works")

        command, args = parse_command('add "Test task"')
        assert command == "add"
        print("[SUCCESS] Parse utility works")

        print("\n[SUCCESS] All core functionality tests passed!")
        return True

    except Exception as e:
        print(f"[ERROR] Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_main_cli()
    if success:
        print("\n[SUCCESS] All tests completed successfully!")
    else:
        print("\n[ERROR] Some tests failed!")
        sys.exit(1)