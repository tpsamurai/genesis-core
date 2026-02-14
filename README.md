# Genesis Core

Open Source Ontology for Identification and Access Management

## Overview

Genesis Core provides a comprehensive ontology for identity and access management (IAM), along with GeneQL, a specialized query language for querying and manipulating the ontology. The system is designed to be flexible, scalable, and easy to integrate into existing applications.

## Features

- **Well-Defined Ontology**: Complete schema for users, groups, resources, permissions, and policies
- **GeneQL Query Language**: Intuitive query language with implementations in JavaScript/TypeScript and Python
- **Database Agnostic**: Supports PostgreSQL, MySQL, and SQLite
- **Security First**: Built-in audit logging, policy-based access control, and time-limited permissions
- **Production Ready**: Comprehensive documentation, deployment guides, and best practices

## Repository Structure

```
genesis-core/
├── schema/              # Database schema for Genesis 1.0 ontology
│   ├── ontology.sql     # Core database schema
│   ├── entities.json    # Entity definitions
│   └── relationships.json # Relationship mappings
├── geneql/              # GeneQL query language implementations
│   ├── javascript/      # JavaScript/TypeScript implementation
│   └── python/          # Python implementation
├── docs/                # Documentation
│   ├── developer-guide/ # Developer documentation
│   └── implementation-guide/ # Implementation and deployment guides
├── public/              # Public-facing website
│   └── index.html       # Landing page
└── releases/            # Release information and downloads
```

## Quick Start

### Installation

#### JavaScript/TypeScript
```bash
npm install @genesis/geneql
```

#### Python
```bash
pip install genesis-geneql
```

### Database Setup

```bash
# PostgreSQL
psql -U postgres -d genesis -f schema/ontology.sql

# MySQL (adapt SQL for MySQL syntax)
mysql -u root -p genesis < schema/ontology.sql
```

### Basic Usage

#### JavaScript
```javascript
const { GeneQL } = require('@genesis/geneql');

const geneql = new GeneQL({
  host: 'localhost',
  database: 'genesis'
});

// Check access
const hasAccess = await geneql.checkAccess(userId, resourceId, 'read');

// Grant permission
await geneql.grantAccess(userId, resourceId, 'write');
```

#### Python
```python
from geneql import GeneQL

geneql = GeneQL(
    host='localhost',
    database='genesis'
)

# Check access
has_access = geneql.check_access(user_id, resource_id, 'read')

# Grant permission
geneql.grant_access(user_id, resource_id, 'write')
```

## Documentation

- **[Developer Guide](docs/developer-guide/)** - Technical documentation for developers
- **[Implementation Guide](docs/implementation-guide/)** - Deployment and production guides
- **[Schema Documentation](schema/)** - Ontology schema details
- **[GeneQL Documentation](geneql/)** - Query language reference

## GeneQL Syntax

GeneQL provides a simple, declarative syntax for working with the ontology:

```geneql
# Retrieve entities
GET User WHERE username = "john.doe"
GET Group WHERE name = "administrators"

# Check access
CHECK User.canAccess(Resource) WHERE User.id = "user123" AND Resource.id = "res456"

# Grant/Revoke permissions
GRANT read TO User ON Resource
REVOKE write FROM User ON Resource
```

## Core Concepts

### Entities

- **User**: Identity in the system
- **Group**: Collection of users
- **Resource**: Protected asset or object
- **Permission**: Defined action that can be performed
- **AccessPolicy**: Rules governing access decisions

### Relationships

- Users belong to Groups (Membership)
- Users own Resources (Ownership)
- Users and Groups have Permissions on Resources (Access)
- Access Policies apply to Resources (Policy Assignment)

## Development

### Prerequisites
- Node.js 18+ (for JavaScript implementation)
- Python 3.8+ (for Python implementation)
- PostgreSQL 12+, MySQL 8+, or SQLite 3.35+

### Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- **Website**: [Genesis Core](https://tpsamurai.github.io/genesis-core)
- **Documentation**: [Full Documentation](docs/)
- **GitHub**: [Repository](https://github.com/tpsamurai/genesis-core)
- **Issues**: [Issue Tracker](https://github.com/tpsamurai/genesis-core/issues)

## Version

Current Version: **1.0.0-alpha** (February 2026)

---

Copyright © 2026 The Prompt Samurai
