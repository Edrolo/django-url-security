# Import the fixture file based on the DEFAULT_FIXTURE_MODULE setting
from importlib import import_module

from .core import DEFAULT_FIXTURE_MODULE

"""
This imports your fixture file specified in the DEFAULT_FIXTURE_MODULE setting
Once this is imported, you can access the fixtures defined in that file
by including the name of the fixture factory functions in the URL security spec file
e.g. 'poll_question' in the example_project/url_security_fixtures.py file
"""
# TODO: Allow manually specifying the fixture module
fixture_module_name = DEFAULT_FIXTURE_MODULE

try:
    fixture_module = import_module(fixture_module_name)
except ImportError:
    if fixture_module_name != DEFAULT_FIXTURE_MODULE:
        # If the fixture module has been specified and isn't there, raise an error
        raise
    else:
        # If the fixture module is the default but isn't there, ignore it.
        fixture_module = None
