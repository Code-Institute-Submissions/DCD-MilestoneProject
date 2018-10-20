from app import *
import datetime
from datetime import datetime as dt
import unittest

"""
To test if all direct routes that render a template can be reached and if the correct template has been used.
"""
class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'

    def test_index(self):
        response = self.app.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_index_contains_correct_html(self):
        response = self.app.get('/', content_type="html/text")
        self.assertTrue(b'<div class="col s12 m12 l6" id="cuisine_pie"></div>' in response.data)

    def test_login(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_login_contains_correct_html(self):
        response = self.app.get('/', content_type="html/text")
        self.assertTrue(b'<h2>User Login</h2>' in response.data)

    def test_register(self):
        response = self.app.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_login_contains_correct_html(self):
        response = self.app.get('/register', content_type="html/text")
        self.assertTrue(b'<h2>User Registeration</h2>' in response.data)

    def test_logout(self):
        response = self.app.get('/logout', content_type="html/text")
        self.assertEqual(response.status_code, 302) # Redirected to index

    def test_add_recipe(self):
        response = self.app.get('/add_recipe', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_contains_correct_html(self):
        response = self.app.get('/add_recipe', content_type="html/text")
        self.assertTrue(b'<h3>Add Recipe</h3>' in response.data)

    def test_new_arrivals(self):
        response = self.app.get('/new_arrivals', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_new_arrivals_contains_correct_html(self):
        response = self.app.get('/new_arrivals', content_type="html/text")
        self.assertTrue(b'<h2>New Arrivals</h2>' in response.data)

    def test_most_popular(self):
        response = self.app.get('/most_popular', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_most_popular_contains_correct_html(self):
        response = self.app.get('/most_popular', content_type="html/text")
        self.assertTrue(b'<h2>Most Popular</h2>' in response.data)

    def test_most_upvote(self):
        response = self.app.get('/most_upvote', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_most_upvote_contains_correct_html(self):
        response = self.app.get('/most_upvote', content_type="html/text")
        self.assertTrue(b'<h2>Most Likes</h2>' in response.data)

    def test_guest_recipes(self):
        response = self.app.get('/guest_recipes', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_guest_recipes_contains_correct_html(self):
        response = self.app.get('/guest_recipes', content_type="html/text")
        self.assertTrue(b'<h2>Capricious Recipes</h2>' in response.data)

    def test_custom_search(self):
        response = self.app.get('/custom_search', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_custom_search_contains_correct_html(self):
        response = self.app.get('/custom_search', content_type="html/text")
        self.assertTrue(b'<h3>Custom Search</h3>' in response.data)
        self.assertTrue(b'<h6>Search for particular recipes with specific requirements</h6>' in response.data)

if __name__ == '__main__':
    unittest.main()
