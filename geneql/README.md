# GeneQL Query Language

GeneQL (Genesis Query Language) is a specialized query language for querying the Genesis ontology. It provides a simple, intuitive syntax for accessing and manipulating identity and access management data.

## Structure

- `javascript/` - JavaScript/TypeScript implementation
- `python/` - Python implementation

## Syntax Overview

GeneQL provides a declarative way to query the Genesis ontology:

```geneql
GET User WHERE username = "john.doe"
GET Group.members WHERE Group.name = "administrators"
CHECK User.canAccess(Resource) WHERE User.id = "user123" AND Resource.id = "res456"
GRANT Permission TO User ON Resource
REVOKE Permission FROM User ON Resource
```

## Features

- **Entity Queries**: Retrieve entities by attributes
- **Relationship Traversal**: Navigate relationships between entities
- **Access Checks**: Verify if users/groups have permissions
- **Permission Management**: Grant and revoke access
- **Policy Evaluation**: Apply access policies to authorization decisions

## Language Implementations

Both JavaScript and Python implementations provide:
- Parser for GeneQL syntax
- Query executor against the ontology database
- Type-safe API for programmatic queries
- Command-line interface for interactive queries

## Getting Started

See the README in each language directory for installation and usage instructions.
