import url_security_fixtures

from django_url_security import url_security


class MyTestCase(url_security.UrlSecurityTestCase):
    url_fixture_module = url_security_fixtures
