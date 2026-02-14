# Genesis Core Releases

This directory contains information about Genesis Core releases and download links.

## Current Version

**Version 1.0.0** (Alpha) - February 2026

This is the initial alpha release of Genesis Core.

## Release Files

Releases are published on GitHub: https://github.com/tpsamurai/genesis-core/releases

### What's Included

Each release contains:
- Source code (zip/tar.gz)
- Database schema files
- GeneQL JavaScript/TypeScript package
- GeneQL Python package
- Documentation
- Examples

## Installation

### From npm (JavaScript/TypeScript)
```bash
npm install @genesis/geneql@1.0.0
```

### From PyPI (Python)
```bash
pip install genesis-geneql==1.0.0
```

### From Source
```bash
# Clone the repository
git clone https://github.com/tpsamurai/genesis-core.git
cd genesis-core

# Checkout specific version
git checkout v1.0.0

# Install JavaScript implementation
cd geneql/javascript
npm install
npm run build

# Install Python implementation
cd ../python
pip install -e .
```

## Version History

### v1.0.0 - Alpha Release (February 2026)
- Initial ontology schema for identity and access management
- Core entities: Users, Groups, Resources, Permissions, Access Policies
- GeneQL query language specification
- JavaScript/TypeScript implementation
- Python implementation
- Developer and implementation guides
- Public-facing documentation site

## Upcoming Releases

### v1.1.0 (Planned)
- Additional database adapters
- Enhanced query optimization
- CLI tools for database management
- Migration utilities

### v1.2.0 (Planned)
- REST API server
- GraphQL interface
- Web-based admin console
- Advanced policy engine

## Changelog

For detailed changelog, see [CHANGELOG.md](../CHANGELOG.md)

## Release Notes

Detailed release notes for each version are available on the [GitHub Releases](https://github.com/tpsamurai/genesis-core/releases) page.

## Support

For issues or questions about releases:
- Open an issue on [GitHub](https://github.com/tpsamurai/genesis-core/issues)
- Check the [documentation](../docs/)
- Review [frequently asked questions](../docs/faq.md)

## License

All releases are distributed under the MIT License. See [LICENSE](../LICENSE) for details.
