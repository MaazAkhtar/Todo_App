# Quickstart Guide: Todo CLI Application

## Prerequisites

- Python 3.13+ installed
- UV package manager installed

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run python src/cli/main.py
   ```

## Usage

Once the application is running, you'll see a prompt where you can enter commands:

### Available Commands

- `add "description"` - Add a new todo item
  Example: `add "Buy groceries"`

- `view` - View all todo items
  Example: `view`

- `update <id> "new description"` - Update a todo item's description
  Example: `update 1 "Buy groceries and cook dinner"`

- `complete <id>` - Mark a todo item as complete
  Example: `complete 1`

- `delete <id>` - Delete a todo item
  Example: `delete 1`

- `help` - Show available commands
  Example: `help`

- `quit` or `exit` - Exit the application
  Example: `quit`

### Example Session

```
Todo CLI Application
Enter command (type 'help' for options): add "Buy milk"
Added todo: 1 - Buy milk [ ]
Enter command (type 'help' for options): add "Walk the dog"
Added todo: 2 - Walk the dog [ ]
Enter command (type 'help' for options): view
1 - Buy milk [ ]
2 - Walk the dog [ ]
Enter command (type 'help' for options): complete 1
Marked todo 1 as complete
Enter command (type 'help' for options): view
1 - Buy milk [X]
2 - Walk the dog [ ]
Enter command (type 'help' for options): quit
Goodbye!
```

## Running Tests

To run the unit tests:
```bash
uv run pytest tests/
```

## Development

For development, you can run the application in development mode:
```bash
uv run python -m src.cli.main
```