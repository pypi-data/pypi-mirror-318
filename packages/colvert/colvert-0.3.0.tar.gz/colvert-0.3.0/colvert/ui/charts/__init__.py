from .base import Base
from .line import Line
from .pie import Pie
from .scatter_map import ScatterMap
from .table import Table

__all__ = [
    "Pie",
    "Line",
    "Table",
    "ScatterMap"
]


def get_all() -> list[type[Base]]:
    """Return all available chart classes."""
    return [Pie, Line, Table, ScatterMap]