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
        self.assertIn(b'<div class="col s12 m12 l6" id="cuisine_pie"></div>', response.data)

    def test_login(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_login_contains_correct_html(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertIn(b'<h2>User Login</h2>', response.data)

    def test_register(self):
        response = self.app.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_register_contains_correct_html(self):
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
        self.assertIn(b'<h3>Add Recipe</h3>', response.data)

    def test_new_arrivals(self):
        response = self.app.get('/new_arrivals', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_new_arrivals_contains_correct_html(self):
        response = self.app.get('/new_arrivals', content_type="html/text")
        self.assertIn(b'<h2>New Arrivals</h2>', response.data)

    def test_most_popular(self):
        response = self.app.get('/most_popular', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_most_popular_contains_correct_html(self):
        response = self.app.get('/most_popular', content_type="html/text")
        self.assertIn(b'<h2>Most Popular</h2>', response.data)

    def test_most_upvote(self):
        response = self.app.get('/most_upvote', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_most_upvote_contains_correct_html(self):
        response = self.app.get('/most_upvote', content_type="html/text")
        self.assertIn(b'<h2>Most Likes</h2>', response.data)

    def test_guest_recipes(self):
        response = self.app.get('/guest_recipes', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_guest_recipes_contains_correct_html(self):
        response = self.app.get('/guest_recipes', content_type="html/text")
        self.assertIn(b'<h2>Capricious Recipes</h2>', response.data)

    def test_custom_search(self):
        response = self.app.get('/custom_search', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_custom_search_contains_correct_html(self):
        response = self.app.get('/custom_search', content_type="html/text")
        self.assertIn(b'<h3>Custom Search</h3>', response.data)
        self.assertIn(b'<h6>Search for particular recipes with specific requirements</h6>', response.data)

    def test_login_redirect(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        response = self.app.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 302) # Redirected to index

    def test_register_redirect(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        response = self.app.get('/register', content_type="html/text")
        self.assertEqual(response.status_code, 302) # Redirected to index

    def test_user_page(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        response = self.app.get('/user/admin', content_type="html/text") # user 'admin' exists in database
        self.assertIn(b'<p>Here is a list of the recipes you created.</p>', response.data)

    def test_all_recipes(self):
        response = self.app.get('/all_recipes/1', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_all_recipes_contains_correct_html(self):
        response = self.app.get('/all_recipes/1', content_type="html/text")
        self.assertIn(b'<h2>All Recipes</h2>', response.data)

    def test_recipes_by_cuisine(self):
        response = self.app.get('/recipes_by_cuisine/Japanese/1', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_recipes_by_cuisine_contains_correct_html(self):
        response = self.app.get('/recipes_by_cuisine/Japanese/1', content_type="html/text")
        self.assertIn(b'<h2>Japanese Recipes</h2>', response.data)

    def test_recipes_by_origin(self):
        response = self.app.get('/recipes_by_origin/Japan/1', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_recipes_by_origin_contains_correct_html(self):
        response = self.app.get('/recipes_by_origin/Japan/1', content_type="html/text")
        self.assertIn(b'<h2>Recipes from Japan</h2>', response.data)

"""
To test whether user authentication behaves as expected
"""
class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'
        return app

    def test_login(self):
        response = self.app.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)
        self.assertIn(b'<h3 class="white-text">Hi, admin</h3>', response.data)

    def test_login_wrong_password(self):
        response = self.app.post('/login', data=dict(username='admin', password='wrong_password'), follow_redirects=True)
        self.assertIn(b'Invalid username/password combination', response.data)

    def test_register(self):
        response = self.app.post('/register', data=dict(username='testuser', password='testuser'), follow_redirects=True)
        self.assertIn(b'<h3 class="white-text">Hi, testuser</h3>', response.data)
        # Removing test data after assertion
        mongo = PyMongo(app)
        testdata = mongo.db.users.find_one({'username': 'testuser'})
        if testdata:
            mongo.db.users.delete_one({'username': 'testuser'})

    def test_register_with_reserved_name(self):
        response = self.app.post('/register', data=dict(username='guest', password='password'), follow_redirects=True)
        self.assertIn(b'This is a reserved name, please choose another name.', response.data)

    def test_register_with_existing_user(self):
        response = self.app.post('/register', data=dict(username='admin', password='admin'), follow_redirects=True)
        self.assertIn(b'Username already exists!', response.data)

"""
To test if recipes related CRUD operation behaves as expected
"""
class TestRecipesCRUD(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'
        return app

if __name__ == '__main__':
    unittest.main()
