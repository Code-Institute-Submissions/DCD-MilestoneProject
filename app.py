import os
from flask import Flask, redirect, render_template, request, url_for, session, flash
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FieldList
from wtforms.validators import InputRequired, Length
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_SECRET_KEY' 
app.config['MONGO_DBNAME'] = 'dcd-milestone'
app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds243041.mlab.com:43041/dcd-milestone'

mongo = PyMongo(app)

def categorise(category_name, user_input):
    output = []
    for key, val in user_input.items():
        if category_name in key:
            output.append(val)
    
    return output

class UserForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(max=20)])
    
    
@app.route('/')
def index():
    new_arrivals = mongo.db.recipes.find().sort([('time_created', -1)]).limit(5)
    most_popular = mongo.db.recipes.find().sort([('views', -1)]).limit(5)
    most_upvote = mongo.db.recipes.find().sort([('upvote_count', -1)]).limit(5)
    random_pointer = mongo.db.recipes.find({"author": 'guest' }).sort([('time_created', -1)]).limit(5)
    random = [r for r in random_pointer]
    return render_template('index.html', new_arrivals=new_arrivals, most_popular=most_popular, most_upvote=most_upvote, random=random)
    
@app.route('/login', methods=['GET',  'POST'])
def login():
    form = UserForm()
    
    if form.validate_on_submit():
        users = mongo.db.users
        login_user = users.find_one({'username': form.username.data})
        if login_user and login_user['password'] == form.password.data:
            session['username'] = form.username.data
            return redirect('/')
        
        flash("Invalid username/password combination", category='error')
    
    return render_template('login.html', form=form)
    
@app.route('/register', methods=['GET',  'POST'])
def register():
    form = UserForm()
    
    if form.validate_on_submit():
        if request.form['username'].strip().lower() == "guest":
            flash("This is a reserved name, please choose another name.")
            return render_template('register.html', form=form)

        users = mongo.db.users
        existing_user = users.find_one({'username': form.username.data})
        
        if existing_user is None:
            users.insert({'username': form.username.data, 'password': form.password.data})
            session['username'] = form.username.data
            return redirect('/')
            
        flash("Username already exists!", category='error')
        
    return render_template('register.html', form=form)
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', countries=mongo.db.countries.find(), allergens=mongo.db.allergens.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    
    # Reorganise all data before inserting into database
    user_input = request.form.to_dict()
    
    # Separate cuisines into a separate list
    cuisines = categorise('cuisine', user_input)
    
    # Separate ingredients into a separate dictionary
    ingredients = []
    unit = []
    for key, val in user_input.items():
        if 'ingredient' in key:
            ingredients.append(val)
        if 'unit' in key:
            unit.append(val)
            
    ingredients_unit = {}
    for x in range(0, len(ingredients)):
        ingredients_unit[ingredients[x]] = unit[x]
    
    instructions = {}
    for key, val in user_input.items():
        if 'instruction' in key:
            instructions[key] = val
    
    author = "guest"
    if 'username' in session:
        author = session['username']
    
    # Reorganise all data into one dictionary before inserting into database
    data = {
        "recipe_name": request.form['name'],
        "origin": request.form['origin'],
        "cuisine": cuisines, # A list
        "ingredients": ingredients_unit, # A dictionary
        "allergens": request.form.getlist('allergens'),
        "instructions": instructions, # A dictionary
        "author": author,
        "views": 0,
        "upvote": [],
        "upvote_count": 0,
        "time_created": datetime.utcnow(),
        "last_modified": datetime.utcnow()
    }
    
    recipes.insert_one(data)

    # Since id is auto generated and there is no way to retrieve it at this point 
    # so using exact parameters user just given to find the newly created recipe and redirect to that

    recipe = mongo.db.recipes.find_one({
        "recipe_name": request.form['name'],
        "origin": request.form['origin'],
        "cuisine": cuisines, # A list
        "ingredients": ingredients_unit, # A dictionary
        "allergens": request.form.getlist('allergens'),
        "instructions": instructions, # A dictionary
        "author": author
        })
    
    return redirect(url_for('view_recipe', recipe_id=recipe['_id']))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {'$inc': {"views": 1}})
    return render_template('view_recipe.html', recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # Only allows users to update recipes they created.
    if 'username' in session and session['username'] == recipe['author']:
        return render_template('edit_recipe.html', recipe=recipe, countries=mongo.db.countries.find(), allergens=mongo.db.allergens.find())

    return redirect('/')

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user_input = request.form.to_dict()
    cuisines = categorise('cuisine', user_input)
    ingredients = []
    unit = []
    for key, val in user_input.items():
        if 'ingredient' in key:
            ingredients.append(val)
        if 'unit' in key:
            unit.append(val)
            
    ingredients_unit = {}
    for x in range(0, len(ingredients)):
        ingredients_unit[ingredients[x]] = unit[x]
    
    instructions = {}
    for key, val in user_input.items():
        if 'instruction' in key:
            instructions[key] = val

    mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)},
        { '$set': {
                    "recipe_name": request.form['name'],
                    "origin": request.form['origin'],
                    "cuisine": cuisines, # A list
                    "ingredients": ingredients_unit, # A dictionary
                    "allergens": request.form.getlist('allergens'),
                    "instructions": instructions,
                    "last_modified": datetime.utcnow()
                }})

    return redirect(url_for('view_recipe', recipe_id=recipe['_id']))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if 'username' in session and session['username'] == recipe['author']:
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
        return redirect(url_for('user_page', user_name=recipe['author']))

    return "You are not authorised to delete this recipe."

@app.route('/upvote/<recipe_id>', methods=['GET', 'POST'])
def upvote(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if 'username' in session and session['username'] not in recipe['upvote']:
        recipe['upvote'].append(session['username'])
    elif 'username' in session and session['username'] in recipe['upvote']:
        recipe['upvote'].remove(session['username'])

    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
            { '$set': {
                "upvote": recipe['upvote'],
                "upvote_count": len(recipe['upvote'])
            }})

    return redirect(url_for('view_recipe', recipe_id=recipe['_id']))

@app.route('/user/<user_name>')
def user_page(user_name):
    if 'username' in session:
        pointer = mongo.db.recipes.find({"author": user_name })
        recipes = [p for p in pointer]
        return render_template('user_page.html', recipes=recipes)

    return redirect('/')

@app.route('/new_arrivals')
def new_arrivals():
    new_arrivals = mongo.db.recipes.find().sort([('time_created', -1)]).limit(20)
    return render_template('new_arrivals.html', new_arrivals=new_arrivals)

@app.route('/most_popular')
def most_popular():
    most_popular = mongo.db.recipes.find().sort([('views', -1)]).limit(20)
    return render_template('most_popular.html', most_popular=most_popular)

@app.route('/most_upvote')
def most_upvote():
    most_upvote = mongo.db.recipes.find().sort([('upvote_count', -1)]).limit(5)
    return render_template('most_upvote.html', most_upvote=most_upvote)

@app.route('/guest_recipes')
def guest_recipes():
    random_pointer = mongo.db.recipes.find({"author": 'guest' }).sort([('time_created', -1)]).limit(20)
    random = [r for r in random_pointer]
    return render_template('guest_recipes.html', random=random)

if __name__ == '__main__':
    if __name__ == '__main__':
        # app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True, threaded=True)
        app.run(debug=True, threaded=True)