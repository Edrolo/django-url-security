"""Test module for django_url_security."""
from django.test import TestCase


# @override_settings(ROOT_URLCONF='django_url_security.tests.urls')
class RelatedTests(TestCase):
    def setUp(self):
        """Create users, categories and entries."""

    def test_running(self):
        """Test that tests are running."""
        assert True


"""
Tests to write:
- Test that tests fail when a specified fixture is missing
"""
