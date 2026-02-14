# GeneQL JavaScript Implementation

JavaScript/TypeScript implementation of the GeneQL query language for the Genesis ontology.

## Installation

```bash
npm install @genesis/geneql
```

## Usage

```javascript
const { GeneQL } = require('@genesis/geneql');

// Initialize with database connection
const geneql = new GeneQL({
  host: 'localhost',
  database: 'genesis',
  // ... other connection options
});

// Execute a query
const result = await geneql.execute('GET User WHERE username = "john.doe"');

// Programmatic API
const user = await geneql.getUser({ username: 'john.doe' });
const canAccess = await geneql.checkAccess(userId, resourceId, 'read');
```

## Development

```bash
npm install
npm run build
npm test
```

## API Reference

See the [API documentation](./docs/api.md) for detailed reference.
