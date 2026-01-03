"""
Integration tests for CLI interface in src/cli/main.py.
"""

import io
import sys
from unittest.mock import patch, MagicMock
from src.cli.main import TodoCLI


class TestCLIBasic:
    """Basic integration tests for the CLI."""

    def test_add_command_integration(self):
        """Test the add command integration."""
        cli = TodoCLI()

        # Mock the input to simulate user adding a todo
        with patch('builtins.input', side_effect=['add "Test task"', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Added todo:" in output
        assert "Test task" in output

    def test_add_command_empty_description(self):
        """Test the add command with empty description."""
        cli = TodoCLI()

        # Mock the input to simulate user adding a todo with empty description
        with patch('builtins.input', side_effect=['add ""', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Error:" in output
        assert "Description cannot be empty" in output

    def test_view_command_integration(self):
        """Test the view command integration."""
        cli = TodoCLI()

        # First add a task, then view it
        with patch('builtins.input', side_effect=['add "Test task for viewing"', 'view', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Added todo:" in output
        assert "Test task for viewing" in output
        assert "[ ]" in output  # Incomplete status indicator

    def test_update_command_integration(self):
        """Test the update command integration."""
        cli = TodoCLI()

        # Add a task, then update it
        with patch('builtins.input', side_effect=['add "Original task"', 'update 1 "Updated task"', 'view', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Added todo:" in output
        assert "Original task" in output
        assert "Updated task" in output
        assert "Updated todo 1 successfully" in output

    def test_complete_command_integration(self):
        """Test the complete command integration."""
        cli = TodoCLI()

        # Add a task, then mark it complete
        with patch('builtins.input', side_effect=['add "Task to complete"', 'complete 1', 'view', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Added todo:" in output
        assert "Task to complete" in output
        assert "Marked todo 1 as complete" in output
        assert "[X]" in output  # Complete status indicator

    def test_delete_command_integration(self):
        """Test the delete command integration."""
        cli = TodoCLI()

        # Add a task, then delete it
        with patch('builtins.input', side_effect=['add "Task to delete"', 'delete 1', 'view', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Added todo:" in output
        assert "Task to delete" in output
        assert "Deleted todo 1 successfully" in output
        assert "No todos in the list" in output  # After deletion, list should be empty

    def test_help_command_integration(self):
        """Test the help command integration."""
        cli = TodoCLI()

        with patch('builtins.input', side_effect=['help', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Available commands:" in output
        assert "add" in output
        assert "view" in output
        assert "update" in output
        assert "complete" in output
        assert "delete" in output


class TestCLIErrorHandling:
    """Error handling integration tests for the CLI."""

    def test_invalid_command_integration(self):
        """Test handling of invalid commands."""
        cli = TodoCLI()

        with patch('builtins.input', side_effect=['invalidcommand', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Unknown command:" in output
        assert "invalidcommand" in output

    def test_update_nonexistent_todo_integration(self):
        """Test updating a non-existent todo."""
        cli = TodoCLI()

        with patch('builtins.input', side_effect=['update 999 "Updated description"', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Error:" in output
        assert "Todo with ID 999 not found" in output

    def test_complete_nonexistent_todo_integration(self):
        """Test marking a non-existent todo as complete."""
        cli = TodoCLI()

        with patch('builtins.input', side_effect=['complete 999', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Error:" in output
        assert "Todo with ID 999 not found" in output

    def test_delete_nonexistent_todo_integration(self):
        """Test deleting a non-existent todo."""
        cli = TodoCLI()

        with patch('builtins.input', side_effect=['delete 999', 'quit']):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                try:
                    cli.run()
                except SystemExit:
                    pass  # Expected when quit command is processed

        output = mock_stdout.getvalue()
        assert "Error:" in output
        assert "Todo with ID 999 not found" in output