"""
Documentation for cksechcalc package.
This can be viewed using help(cksechcalc) or help(cksechcalc.module)

New addition: ver and version in ver.py will work as function without module
"""
__version__ = '0.4.0'

from .add import add
from .subtract import subtract
from .multiply import multiply
from .divide import divide
from .ver import version, ver  # import both to work as function and without function name
