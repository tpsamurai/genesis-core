# Genesis 1.0 Ontology Schema

This directory contains the database schema for the Genesis 1.0 ontology, which provides a framework for identification and access management.

## Structure

- `ontology.sql` - Core database schema for Genesis 1.0
- `entities.json` - Entity definitions for the ontology
- `relationships.json` - Relationship mappings between entities
- `migrations/` - Database migration scripts

## Schema Overview

The Genesis ontology defines the following core concepts:
- **Entities**: Users, Groups, Resources, Permissions
- **Relationships**: Ownership, Membership, Access Rights
- **Policies**: Access control policies and rules

## Usage

The schema is designed to be database-agnostic where possible, with specific implementations provided for:
- PostgreSQL
- MySQL
- SQLite

See individual schema files for implementation details.
