from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolver_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_corect_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))