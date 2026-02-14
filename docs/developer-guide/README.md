# Developer Guide

Welcome to the Genesis Core Developer Guide. This guide will help you understand and work with the Genesis ontology and GeneQL query language.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Core Concepts](#core-concepts)
4. [Working with the Ontology](#working-with-the-ontology)
5. [Using GeneQL](#using-geneql)
6. [API Reference](#api-reference)
7. [Examples](#examples)

## Introduction

Genesis Core is an ontology-based system for identification and access management. It provides:
- A well-defined schema for identity and access concepts
- GeneQL, a specialized query language
- Implementations in JavaScript/TypeScript and Python

## Getting Started

### Prerequisites
- Node.js 18+ (for JavaScript implementation)
- Python 3.8+ (for Python implementation)
- PostgreSQL, MySQL, or SQLite database

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

1. Choose your database (PostgreSQL, MySQL, or SQLite)
2. Run the schema initialization script:

```bash
# For PostgreSQL
psql -U username -d genesis < schema/ontology.sql
```

## Core Concepts

### Entities

The Genesis ontology defines the following core entities:

#### User
Represents an identity in the system.
- Properties: id, username, email, status, metadata
- Relationships: groups, resources, permissions

#### Group
A collection of users for access management.
- Properties: id, name, description, metadata
- Relationships: users, resources, permissions

#### Resource
A protected asset or object in the system.
- Properties: id, name, type, owner_id, metadata
- Relationships: owner, access grants, policies

#### Permission
A defined action that can be performed.
- Properties: id, name, description, scope
- Relationships: users, groups, resources

#### AccessPolicy
Rules that govern access decisions.
- Properties: id, name, policy_type, conditions
- Relationships: resources, creator

### Relationships

Key relationships in the ontology:
- **Membership**: Users belong to Groups
- **Ownership**: Users own Resources
- **Access**: Users and Groups have Permissions on Resources
- **Policies**: Access Policies apply to Resources

## Working with the Ontology

### Schema Files

The ontology is defined in several files:

1. **ontology.sql** - Database schema
2. **entities.json** - Entity definitions
3. **relationships.json** - Relationship mappings

### Extending the Ontology

To add new entities or relationships:

1. Update `entities.json` with new entity definitions
2. Update `relationships.json` with new relationship mappings
3. Create migration scripts in `schema/migrations/`
4. Update the SQL schema accordingly

## Using GeneQL

### Query Syntax

GeneQL provides a simple, declarative syntax:

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

### JavaScript API

```javascript
const { GeneQL } = require('@genesis/geneql');

const geneql = new GeneQL({
  host: 'localhost',
  database: 'genesis',
  username: 'user',
  password: 'pass'
});

// Execute queries
const result = await geneql.execute('GET User WHERE username = "john.doe"');

// Programmatic API
const user = await geneql.getUser({ username: 'john.doe' });
const hasAccess = await geneql.checkAccess(userId, resourceId, 'read');
```

### Python API

```python
from geneql import GeneQL

geneql = GeneQL(
    host='localhost',
    database='genesis',
    username='user',
    password='pass'
)

# Execute queries
result = geneql.execute('GET User WHERE username = "john.doe"')

# Programmatic API
user = geneql.get_user(username='john.doe')
has_access = geneql.check_access(user_id, resource_id, 'read')
```

## API Reference

See the complete API reference for detailed method documentation:
- [JavaScript API Reference](../api-reference/javascript.md)
- [Python API Reference](../api-reference/python.md)

## Examples

### Example 1: User Management

```javascript
// Create a user
const user = await geneql.execute(`
  CREATE User WITH 
    username = "jane.doe",
    email = "jane@example.com"
`);

// Add user to a group
await geneql.execute(`
  ADD User TO Group 
  WHERE User.username = "jane.doe" 
  AND Group.name = "developers"
`);
```

### Example 2: Access Control

```python
# Grant read access to a user
geneql.grant_access(user_id, resource_id, 'read')

# Check if user can write
can_write = geneql.check_access(user_id, resource_id, 'write')

# Apply an access policy
geneql.execute("""
  APPLY Policy TO Resource 
  WHERE Policy.name = "strict-access" 
  AND Resource.type = "confidential"
""")
```

### Example 3: Querying Relationships

```javascript
// Get all users in a group
const members = await geneql.execute(`
  GET User.members WHERE Group.name = "administrators"
`);

// Get all resources owned by a user
const ownedResources = await geneql.execute(`
  GET Resource WHERE Resource.owner_id = "user123"
`);
```

## Next Steps

- Explore the [Implementation Guide](../implementation-guide/) for production deployment
- Check out more [Examples](../examples/)
- Review [Security Best Practices](../implementation-guide/security.md)
- Join our community and contribute!
