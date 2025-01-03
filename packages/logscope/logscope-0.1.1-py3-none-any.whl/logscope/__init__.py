"""
Logscope - Queryable logging with SQLite storage

Logscope provides enhanced logging capabilities with SQLite storage and pretty console output.
"""

from logscope.core import logger, query
from logscope.tracing import trace

__version__ = "0.1.0"
__all__ = ['logger', 'query', 'trace']