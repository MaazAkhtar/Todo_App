# Todo CLI Application

A command-line interface application for managing todo items with in-memory storage.

## Features

- Add new todo items
- View all todo items
- Update todo item descriptions
- Mark todo items as complete
- Delete todo items
- Interactive command-line interface

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, but recommended)

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies (if using UV):
   ```bash
   uv sync
   ```
   Or if using pip:
   ```bash
   pip install -e .
   ```

## Usage

Run the application:

```bash
python -m src.cli.main
```

Or if installed as a package:
```bash
todo-cli
```

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
Type 'help' for available commands or 'quit' to exit.
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

## Project Structure

```
src/
├── models/
│   └── todo.py          # TodoItem data model and TodoList container
├── services/
│   └── todo_manager.py  # Core business logic for todo operations
├── cli/
│   └── main.py          # Interactive CLI interface and command parsing
└── lib/
    └── utils.py         # Utility functions for input validation, formatting, etc.

tests/
├── unit/
│   ├── test_models.py   # Unit tests for data models
│   └── test_services.py # Unit tests for business logic
├── integration/
│   └── test_cli.py      # Integration tests for CLI interface
└── contract/
    └── test_contracts.py # Contract tests for API compliance
```

## Development

### Running Tests

To run the full test suite:
```bash
python -m pytest tests/
```

To run specific test files:
```bash
python -m pytest tests/unit/test_models.py
```

### Architecture

The application follows clean architecture principles with separation of concerns:

- **Models** (`src/models/`): Data structures and basic operations
- **Services** (`src/services/`): Business logic and application rules
- **CLI** (`src/cli/`): User interface and command parsing
- **Lib** (`src/lib/`): Utility functions and helpers

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`python -m pytest tests/`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.