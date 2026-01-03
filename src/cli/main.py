#!/usr/bin/env python3
"""
Interactive CLI interface for the todo application.
"""

import sys
from typing import List
from src.services.todo_manager import TodoManager
from src.lib.utils import parse_command, format_todo_item, validate_todo_description, is_valid_id, display_help


class TodoCLI:
    """
    Interactive CLI interface and command parsing.
    """

    def __init__(self):
        """Initialize the CLI with a todo manager."""
        self.manager = TodoManager()
        self.running = True

    def run(self):
        """Start the interactive CLI loop."""
        print("Todo CLI Application")
        print("Type 'help' for available commands or 'quit' to exit.")

        while self.running:
            try:
                user_input = input("Enter command (type 'help' for options): ").strip()
                if not user_input:
                    continue

                command, args = parse_command(user_input)
                self.execute_command(command, args)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def execute_command(self, command: str, args: List[str]):
        """Execute a command with the given arguments."""
        if command in ['quit', 'exit']:
            self.handle_quit()
        elif command == 'add':
            self.handle_add(args)
        elif command == 'view':
            self.handle_view()
        elif command == 'update':
            self.handle_update(args)
        elif command == 'complete':
            self.handle_complete(args)
        elif command == 'delete':
            self.handle_delete(args)
        elif command == 'help':
            self.handle_help()
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")

    def handle_add(self, args: List[str]):
        """Handle the add command."""
        if len(args) < 1:
            print("Error: Missing description. Usage: add \"description\"")
            return

        description = " ".join(args)
        if not validate_todo_description(description):
            print("Error: Description cannot be empty")
            return

        try:
            todo_item = self.manager.add_todo(description)
            print(f"Added todo: {format_todo_item(todo_item)}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view(self, args: List[str] = None):
        """Handle the view command."""
        todos = self.manager.list_todos()
        if not todos:
            print("No todos in the list.")
        else:
            for todo in todos:
                print(format_todo_item(todo))

    def handle_update(self, args: List[str]):
        """Handle the update command."""
        if len(args) < 2:
            print("Error: Missing ID or description. Usage: update id \"new description\"")
            return

        todo_id_str, *desc_parts = args
        description = " ".join(desc_parts)

        if not is_valid_id(todo_id_str):
            print("Error: Invalid ID format. ID must be a positive integer.")
            return

        if not validate_todo_description(description):
            print("Error: Description cannot be empty")
            return

        todo_id = int(todo_id_str)
        success = self.manager.update_todo(todo_id, description)
        if success:
            print(f"Updated todo {todo_id} successfully")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_complete(self, args: List[str]):
        """Handle the complete command."""
        if len(args) < 1:
            print("Error: Missing ID. Usage: complete id")
            return

        todo_id_str = args[0]

        if not is_valid_id(todo_id_str):
            print("Error: Invalid ID format. ID must be a positive integer.")
            return

        todo_id = int(todo_id_str)
        success = self.manager.mark_complete(todo_id)
        if success:
            print(f"Marked todo {todo_id} as complete")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_delete(self, args: List[str]):
        """Handle the delete command."""
        if len(args) < 1:
            print("Error: Missing ID. Usage: delete id")
            return

        todo_id_str = args[0]

        if not is_valid_id(todo_id_str):
            print("Error: Invalid ID format. ID must be a positive integer.")
            return

        todo_id = int(todo_id_str)
        success = self.manager.delete_todo(todo_id)
        if success:
            print(f"Deleted todo {todo_id} successfully")
        else:
            print(f"Error: Todo with ID {todo_id} not found")

    def handle_help(self, args: List[str] = None):
        """Handle the help command."""
        print(display_help())

    def handle_quit(self):
        """Handle the quit command."""
        self.running = False
        print("Goodbye!")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()