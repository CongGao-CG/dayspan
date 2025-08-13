"""DaySpan - A simple tool to count days between two dates."""

from .calculator import calculate_days, parse_date

try:
    from importlib.metadata import version
    __version__ = version("dayspan")
except ImportError:
    import pkg_resources
    __version__ = pkg_resources.get_distribution("dayspan").version

__author__ = 'Cong Gao'
__all__ = ['calculate_days', 'parse_date']
