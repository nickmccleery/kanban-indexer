# kanban-indexer

`kanban-indexer` is a simple Python library that implements a lexicographic indexing system for ordered collections, such as columns on a Kanban board. It uses a chracter-based system that should allow for an arbitrary number of insertions between any two existing indices without the need for reindexing.

## Features

- Generates string indices composed of characters A-Z
- Uses lexicographic ordering to determine item placement
- Creates new indices at the midpoint between existing indices
- Allows insertions before the first item and after the last item
- Avoids floating-point precision issues by using string comparisons
- Produces human-readable indices

## Installation

You can install `kanban-indexer` using pip:

`pip install kanban-indexer`

## Usage

Here's a quick example of how to use `kanban-indexer`:

```python
from kanban_indexer import compute_intermediate_index, compute_preceding_index, compute_succeeding_index

# Generate an index between "B" and "C"
middle_index = compute_intermediate_index("B", "C")
print(middle_index)  # Output: BM

# Generate an index before "A"
before_b = compute_preceding_index("B")
print(before_b)  # Output: AZ

# Generate an index after "Z"
after_z = compute_succeeding_index("Z")
print(after_z)  # Output: ZB
```

## API Reference

### `compute_intermediate_index(index_before: str, index_after: str) -> str`

Computes the intermediate index between two given indices.

### `compute_preceding_index(index: str) -> str`

Returns the preceding index value based on the given index.

### `compute_succeeding_index(index: str) -> str`

Returns the succeeding index based on the given index.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Development

To set up the development environment:

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the package with development dependencies:
   `pip install -e .[dev]`

### Running Tests

You can run tests using pytest:

`pytest`

### Linting and Formatting

This project uses `ruff` for linting and formatting. To run ruff:

`ruff check .`

To automatically fix issues and format code:

`ruff check --fix .`
