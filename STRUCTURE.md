# Genesis Core - Repository Structure

This document describes the complete repository structure for Genesis Core.

## Overview

Genesis Core is an ontology for identification and access management, consisting of:
- Database schema defining the ontology
- GeneQL query language (JavaScript and Python implementations)
- Comprehensive documentation
- Public-facing website
- Release management

## Directory Structure

```
genesis-core/
├── schema/                      # Genesis 1.0 Ontology Database Schema
│   ├── README.md               # Schema overview and documentation
│   ├── ontology.sql            # Complete SQL schema (Users, Groups, Resources, etc.)
│   ├── entities.json           # Entity definitions with JSON schema
│   └── relationships.json      # Relationship mappings between entities
│
├── geneql/                      # GeneQL Query Language Implementations
│   ├── README.md               # GeneQL overview and syntax guide
│   │
│   ├── javascript/             # JavaScript/TypeScript Implementation
│   │   ├── README.md          # JS-specific documentation
│   │   ├── package.json       # NPM package configuration
│   │   ├── tsconfig.json      # TypeScript configuration
│   │   └── src/
│   │       ├── index.ts       # Main GeneQL client class
│   │       └── parser.ts      # Query parser
│   │
│   └── python/                 # Python Implementation
│       ├── README.md          # Python-specific documentation
│       ├── setup.py           # Python package configuration
│       └── geneql/
│           ├── __init__.py    # Package initialization
│           ├── client.py      # Main GeneQL client class
│           └── parser.py      # Query parser
│
├── docs/                        # Documentation
│   ├── README.md               # Documentation index
│   ├── developer-guide/        # Developer documentation
│   │   └── README.md          # Getting started, API reference, examples
│   └── implementation-guide/   # Production deployment guide
│       └── README.md          # Deployment, security, monitoring
│
├── public/                      # Public-Facing Website
│   ├── README.md               # Website documentation
│   └── index.html             # Landing page with features and examples
│
├── releases/                    # Release Management
│   └── README.md               # Version history and download links
│
├── .gitignore                   # Git ignore rules (Node.js + Python)
├── LICENSE                      # MIT License
├── README.md                    # Main project README
└── STRUCTURE.md                 # This file
```

## Key Components

### Schema (Genesis 1.0 Ontology)
- **ontology.sql**: Complete database schema with:
  - Entities: Users, Groups, Resources, Permissions, Access Policies
  - Relationships: Memberships, Ownership, Access Grants
  - Audit logging and indexes
- **entities.json**: Formal entity definitions using JSON schema
- **relationships.json**: Relationship type definitions and mappings

### GeneQL Query Language
- **JavaScript/TypeScript**: 
  - Modern async/await API
  - Type-safe with TypeScript
  - NPM package ready
- **Python**:
  - Pythonic API with type hints
  - PyPI package ready
  - Python 3.8+ compatible

### Documentation
- **Developer Guide**: Technical documentation for developers
  - Getting started
  - Core concepts
  - API reference
  - Code examples
- **Implementation Guide**: Production deployment guide
  - System requirements
  - Installation steps
  - Security configuration
  - Performance tuning
  - Monitoring and maintenance

### Public Website
- Responsive landing page
- Feature showcase
- Quick start examples
- Links to documentation and downloads

### Releases
- Version history
- Download instructions
- Changelog
- Release notes

## Usage

### For Developers
1. Read the [Developer Guide](docs/developer-guide/README.md)
2. Install GeneQL for your language (JS or Python)
3. Set up the database using schema/ontology.sql
4. Start building with the GeneQL API

### For Operations/DevOps
1. Read the [Implementation Guide](docs/implementation-guide/README.md)
2. Follow deployment instructions
3. Configure security and monitoring
4. Review best practices

### For End Users
1. Visit the public website (public/index.html)
2. Download releases from the releases page
3. Follow quick start guides

## File Statistics

- Total files: 23+
- Total lines added: 2,235+
- Languages: SQL, JavaScript/TypeScript, Python, HTML, JSON, Markdown
- Documentation: 1,000+ lines
- Code: 700+ lines
- Configuration: 100+ lines

## Next Steps

This structure provides a foundation for:
- Further ontology refinement
- GeneQL parser implementation
- Database connector implementations
- REST API server
- Web-based admin console
- Additional documentation
- Test suites
- CI/CD pipelines

## License

MIT License - See [LICENSE](LICENSE) file for details.
