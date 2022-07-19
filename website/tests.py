from django.test import TestCase


class HomepageViewTests(TestCase):
    def test_homepage_get(self):
            '''Test if the home page loads properly'''
            response = self.client.get('')
            self.assertEqual(response.status_code, 200)
