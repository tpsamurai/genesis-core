"""
GeneQL - Genesis Query Language
Python implementation for querying the Genesis ontology
"""

from .client import GeneQL
from .parser import GeneQLParser, QueryType

__version__ = "1.0.0"
__all__ = ["GeneQL", "GeneQLParser", "QueryType"]
