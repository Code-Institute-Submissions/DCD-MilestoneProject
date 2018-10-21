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

    def test_view_recipe_with_invalid_id(self):
        response = self.app.get('/view_recipe/111122223333444455556666', follow_redirects=True)
        self.assertIn(b'Invalid recipe id', response.data)

    def test_edit_recipe_with_invalid_id(self):
        response = self.app.get('/edit_recipe/111122223333444455556666', follow_redirects=True)
        self.assertIn(b'Invalid recipe id', response.data)

    def test_update_recipe_with_invalid_id(self):
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        response = self.app.post('/update_recipe/111122223333444455556666', data=testdata, follow_redirects=True)
        self.assertIn(b'Invalid recipe id', response.data)

    def test_delete_recipe_with_invalid_id(self):
        response = self.app.get('/delete_recipe/111122223333444455556666', follow_redirects=True)
        self.assertIn(b'Invalid recipe id', response.data)

    def test_upvote_with_invalid_id(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        response = self.app.get('/upvote/111122223333444455556666', follow_redirects=True)
        self.assertIn(b'Invalid recipe id', response.data)

    def test_user_page_with_invalid_username(self):
        response = self.app.get('/user/nonuser', follow_redirects=True)
        self.assertIn(b'No such user', response.data)

    def test_user_page_when_not_logged_in(self):
        response = self.app.get('/user/admin', follow_redirects=True)
        self.assertIn(b'<h2>User Login</h2>', response.data) # Redirected to login page

    def test_user_page_invalid_access(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        response = self.app.get('/user/colman')
        self.assertEqual(response.status_code, 302) # Redirected to admin's user page

"""
To test whether user authentication behaves as expected
"""
class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'

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
        testdata = mongo.db.users.find_one({'username': 'testuser'})
        if testdata:
            mongo.db.users.delete_one(testdata)

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

    def test_add_recipe_as_guest(self):
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        response = self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        self.assertTrue(response.status_code, 302) # Redirected to view_recipe page
        self.assertIn(b'Test Recipe <span class="subtext">by</span> guest', response.data) # Not logged in, so author is set to 'guest'
        # Removing test data after assertion
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            mongo.db.recipes.delete_one(recipe)

    def test_add_recipe_as_named_user(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        response = self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        self.assertTrue(response.status_code, 302) # Redirected to view_recipe page
        self.assertIn(b'Test Recipe <span class="subtext">by</span> admin', response.data) # Author is set to user logged in (i.e. admin)
        # Removing test data after assertion
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            mongo.db.recipes.delete_one(recipe)

    # To test if the edit recipe page can be reached
    def test_edit_recipe(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.get('/edit_recipe/' + str(recipe['_id']))
            self.assertEqual(response.status_code, 200) # Edit recipe page can be reached without problem
            self.assertIn(b'<h3>Edit Recipe</h3>', response.data) # Correct template used
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    # To test if update operation actually works
    def test_update_recipe(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        newdata = {
            "name": "test recipe new", # Changed name
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1", # Removed ingredient 2
            "instruction_1": "instruction 1",
            "instruction_2": "instruction 2" # Added new instruction
        }
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.post('/update_recipe/' + str(recipe['_id']), data=newdata, follow_redirects=True)
            self.assertIn(b'Test Recipe New', response.data)
            self.assertIn(b'instruction 2', response.data)
            self.assertNotIn(b'ingredient 2', response.data)
            mongo.db.recipes.delete_one({'recipe_name': 'test recipe new'})
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    # To test if app behaves as expected when user attempt to update recipe other than their own
    def test_invalid_update_recipe(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        with self.app.session_transaction() as sess:
            sess['username'] = 'user1' # Assumed user 'user1' logged in
        newdata = {
            "name": "test recipe new", # Changed name
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1", # Removed ingredient 2
            "instruction_1": "instruction 1",
            "instruction_2": "instruction 2" # Added new instruction
        }
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.get('/edit_recipe/' + str(recipe['_id']), follow_redirects=True)
            self.assertIn(b"You are not the author of that recipe, hence you are not allowed to edit.", response.data)
            response = self.app.post('/update_recipe/' + str(recipe['_id']), data=newdata, follow_redirects=True)
            self.assertIn(b"You are not the author of that recipe, hence you are not allowed to edit.", response.data)
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    def test_delete_recipe(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            xcount = mongo.db.recipes.count_documents({})
            response = self.app.get('/delete_recipe/' + str(recipe['_id']), follow_redirects=True)
            ycount = mongo.db.recipes.count_documents({})
            self.assertNotEqual(xcount, ycount)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    def test_invalid_delete_recipe(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        with self.app.session_transaction() as sess:
            sess['username'] = 'user1' # Assumed user 'user1' logged in
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.get('/delete_recipe/' + str(recipe['_id']), follow_redirects=True)
            self.assertIn(b'You are not the author of that recipe, hence you are not allowed to delete.', response.data)
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

"""
To test if upvote feature behaves as expected
"""
class TestUpvote(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'

    def test_upvote(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.get('/upvote/' + str(recipe['_id']))
            recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
            self.assertEqual(recipe['upvote_count'], 1)
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    def test_undo_upvote(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            self.app.get('/upvote/' + str(recipe['_id']))
            response = self.app.get('/upvote/' + str(recipe['_id']))
            recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
            self.assertEqual(recipe['upvote_count'], 0)
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

    def test_invalid_upvote(self):
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)
        with self.app.session_transaction() as sess:
            sess.pop('username', None) # Assumed user 'admin' logged out
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            response = self.app.get('/upvote/' + str(recipe['_id']), follow_redirects=True)
            self.assertIn(b'<h2>User Login</h2>', response.data) # Redirected to login page
            mongo.db.recipes.delete_one(recipe)
        else: # pragma: no cover
            self.fail("Were not able to retrieve the recipe created.")

"""
To test if upvote feature behaves as expected
"""
class TestCustomSearch(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['SERVER_NAME'] = 'localhost.localdomain'
        app.config['SECRET_KEY'] = 'secret_key'
        with self.app.session_transaction() as sess:
            sess['username'] = 'admin' # Assumed user 'admin' logged in
        testdata = {
            "name": "test recipe",
            "origin": "Japan",
            "cuisine": "Japanese",
            "ingredient_1": "ingredient 1",
            "unit_1": "unit 1",
            "ingredient_2": "ingredient 2",
            "unit_2": "unit 2",
            "instruction_1": "instruction 1"
        }
        self.app.post('/insert_recipe',data=testdata ,follow_redirects=True)

    def tearDown(self):
        recipe = mongo.db.recipes.find_one({'recipe_name': 'test recipe'})
        if recipe:
            mongo.db.recipes.delete_one(recipe)

    """
    Need to test several patterns of search criteria to make sure all process
    in composing the search query are tested.
    """
    def test_custom_search_case1(self):
        searchcriteria = { # These 3 criteria need to be passed manually whilst the rest are processed
            "name": "test",
            "ingredient_1": "", # did not specify any ingredient as search criteria
            "author": "", # did not specify any author as search criteria
        }
        response = self.app.post('/custom_search/search', data=searchcriteria, follow_redirects=True)
        self.assertIn(b'Test Recipe', response.data)

    def test_custom_search_case2(self):
        searchcriteria = { # These 3 criteria need to be passed manually whilst the rest are processed
            "name": "", # did not specify any recipe name
            "ingredient_1": "ingredient 1",
            "author": "", # did not specify any author as search criteria
        }
        response = self.app.post('/custom_search/search', data=searchcriteria, follow_redirects=True)
        self.assertIn(b'Test Recipe', response.data)

    def test_custom_search_case3(self):
        searchcriteria = { # These 3 criteria need to be passed manually whilst the rest are processed
            "name": "", # Nothing is specified
            "ingredient_1": "",
            "author": "",
        }
        response = self.app.post('/custom_search/search', data=searchcriteria, follow_redirects=True)
        self.assertIn(b'<h3>Custom Search</h3>', response.data) # Search is not processed

    def test_custom_search_case4(self):
        searchcriteria = { # These 3 criteria need to be passed manually whilst the rest are processed
            "name": "",
            "ingredient_1": "",
            "author": "admin",
        }
        response = self.app.post('/custom_search/search', data=searchcriteria, follow_redirects=True)
        self.assertIn(b'Test Recipe', response.data)

    def test_custom_search_case5(self):
        searchcriteria = { # These 3 criteria need to be passed manually whilst the rest are processed
            "name": "",
            "ingredient_1": "",
            "author": "",
            "allergens": "Gluten"
        }
        response = self.app.post('/custom_search/search', data=searchcriteria, follow_redirects=True)
        self.assertNotIn(b'Test Recipe', response.data)

if __name__ == '__main__':
    unittest.main()
