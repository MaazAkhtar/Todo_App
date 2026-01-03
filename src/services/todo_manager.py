"""
Todo manager service for handling business logic operations.
"""

from typing import List, Optional
from src.models.todo import TodoItem, TodoList


class TodoManager:
    """
    Core business logic for todo operations.
    """

    def __init__(self):
        """Initialize the todo manager with an empty todo list."""
        self.todo_list = TodoList()

    def add_todo(self, description: str) -> TodoItem:
        """
        Add a new todo item with unique ID assignment.

        Args:
            description: The description of the new todo item

        Returns:
            The newly created TodoItem

        Raises:
            ValueError: If description is empty
        """
        if not description.strip():
            raise ValueError("Description cannot be empty")

        return self.todo_list.add_item(description.strip())

    def list_todos(self) -> List[TodoItem]:
        """
        Get all todo items in the list.

        Returns:
            A list of all TodoItem objects
        """
        return self.todo_list.list_all()

    def get_todo(self, todo_id: int) -> Optional[TodoItem]:
        """
        Get a specific todo item by ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem if found, None otherwise
        """
        return self.todo_list.get_item(todo_id)

    def update_todo(self, todo_id: int, description: str) -> bool:
        """
        Update an existing todo item's description.

        Args:
            todo_id: The ID of the todo item to update
            description: The new description

        Returns:
            True if the item was updated, False if the item was not found

        Raises:
            ValueError: If description is empty
        """
        if not description.strip():
            raise ValueError("Description cannot be empty")

        return self.todo_list.update_item(todo_id, description.strip())

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo item to mark as complete

        Returns:
            True if the item was marked complete, False if the item was not found
        """
        return self.todo_list.mark_complete(todo_id)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was deleted, False if the item was not found
        """
        return self.todo_list.delete_item(todo_id)

    def get_next_id(self) -> int:
        """
        Get the next available ID.

        Returns:
            The next available ID
        """
        return self.todo_list.get_next_id()