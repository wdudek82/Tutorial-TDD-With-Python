from django.test import TestCase


class HomePageTest(TestCase):

    # def test_root_url_resolver_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    def test_home_page_returns_corect_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')

        # html = response.content.decode('utf-8')
        # self.assertTrue(html.startswith('<html lang="en">'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))  # Remove any whitespace at the end of the .html file
        self.assertTemplateUsed(response, 'lists/home.html')
