"""
Todo data models for the CLI application.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class TodoItem:
    """
    Represents a single task in the todo list.

    Attributes:
        id: Unique identifier for the todo item
        description: Text description of the task
        completed: Status indicating whether the task is completed
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the TodoItem after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")
        if not self.description or not isinstance(self.description, str):
            raise ValueError("Description must be a non-empty string")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")


class TodoList:
    """
    Collection of TodoItem objects managed in memory.
    """

    def __init__(self):
        """Initialize an empty todo list with next_id counter."""
        self.items: Dict[int, TodoItem] = {}
        self.next_id: int = 1

    def add_item(self, description: str) -> TodoItem:
        """
        Add a new todo item and assign the next available ID.

        Args:
            description: The description of the new todo item

        Returns:
            The newly created TodoItem

        Raises:
            ValueError: If description is empty
        """
        if not description:
            raise ValueError("Description cannot be empty")

        item = TodoItem(id=self.next_id, description=str(description))
        self.items[self.next_id] = item
        self.next_id += 1
        return item

    def get_item(self, item_id: int) -> Optional[TodoItem]:
        """
        Retrieve a todo item by its ID.

        Args:
            item_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem if found, None otherwise
        """
        return self.items.get(item_id)

    def update_item(self, item_id: int, description: str) -> bool:
        """
        Update an existing item's description.

        Args:
            item_id: The ID of the todo item to update
            description: The new description

        Returns:
            True if the item was updated, False if the item was not found
        """
        if not description:
            raise ValueError("Description cannot be empty")

        if item_id in self.items:
            self.items[item_id].description = str(description)
            return True
        return False

    def mark_complete(self, item_id: int) -> bool:
        """
        Update an item's status to completed.

        Args:
            item_id: The ID of the todo item to mark as complete

        Returns:
            True if the item was marked complete, False if the item was not found
        """
        if item_id in self.items:
            self.items[item_id].completed = True
            return True
        return False

    def delete_item(self, item_id: int) -> bool:
        """
        Remove an item by its ID.

        Args:
            item_id: The ID of the todo item to delete

        Returns:
            True if the item was deleted, False if the item was not found
        """
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    def list_all(self) -> List[TodoItem]:
        """
        Return all items in the collection.

        Returns:
            A list of all TodoItem objects in the collection
        """
        return list(self.items.values())

    def get_next_id(self) -> int:
        """
        Get the next available ID without incrementing the counter.

        Returns:
            The next available ID
        """
        return self.next_id