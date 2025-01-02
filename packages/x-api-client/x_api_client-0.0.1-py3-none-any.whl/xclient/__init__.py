from importlib.metadata import version

from .client import XError, XClient

__all__ = ["XError", "XClient"]
__version__ = version("xclient")
