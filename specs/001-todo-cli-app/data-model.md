# Data Model: Todo CLI Application

## TodoItem Entity

**Name**: TodoItem
**Description**: Represents a single task in the todo list
**Fields**:
- `id` (int): Unique identifier for the todo item (auto-assigned)
- `description` (str): Text description of the task
- `completed` (bool): Status indicating whether the task is completed (default: False)

**Validation Rules**:
- `id` must be a positive integer
- `description` must not be empty or None
- `completed` must be a boolean value

**State Transitions**:
- Initial state: `completed = False`
- Can transition to: `completed = True` (via mark complete operation)
- Cannot transition back to incomplete once marked complete (unless explicitly updated)

## TodoList Container

**Name**: TodoList
**Description**: Collection of TodoItem objects managed in memory
**Fields**:
- `items` (dict): Dictionary mapping ID to TodoItem objects
- `next_id` (int): The next available ID to assign (auto-incrementing)

**Operations**:
- Add TodoItem: Adds a new item and assigns the next available ID
- Get TodoItem: Retrieves an item by its ID
- Update TodoItem: Modifies an existing item's description
- Mark Complete: Updates an item's status to completed
- Delete TodoItem: Removes an item by its ID
- List All: Returns all items in the collection

**Validation Rules**:
- No duplicate IDs allowed
- Items must have valid TodoItem structure
- Operations on non-existent IDs must return appropriate error messages