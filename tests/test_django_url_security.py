"""Test module for django_url_security."""

from django_url_security import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Matt Fisher"
    assert __email__ == "m@ttfisher.com"
    assert __version__ == "0.0.0"
