# GeneQL Python Implementation

Python implementation of the GeneQL query language for the Genesis ontology.

## Installation

```bash
pip install genesis-geneql
```

Or from source:

```bash
cd geneql/python
pip install -e .
```

## Usage

```python
from geneql import GeneQL

# Initialize with database connection
geneql = GeneQL(
    host='localhost',
    database='genesis',
    # ... other connection options
)

# Execute a query
result = geneql.execute('GET User WHERE username = "john.doe"')

# Programmatic API
user = geneql.get_user(username='john.doe')
can_access = geneql.check_access(user_id, resource_id, 'read')
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

## API Reference

See the [API documentation](./docs/api.md) for detailed reference.
