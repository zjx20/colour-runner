import sys

if sys.version_info < (2, 7):
    from unittest2 import runner
else:
    from unittest import runner

from .result import ColourTextTestResult


class ColourTextTestRunner(runner.TextTestRunner):
    """A test runner that uses colour in its output"""
    resultclass = ColourTextTestResult
