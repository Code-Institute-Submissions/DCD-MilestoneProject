import os
from flask import Flask, redirect, render_template, request, url_for, session, flash
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FieldList
from wtforms.validators import InputRequired, Length
from bson.objectid import ObjectId

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
    return render_template('index.html')
    
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
    if 'user' in session:
        author = session['user']
    
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
        "upvote": 0
    }
    
    recipes.insert_one(data)
    
    return redirect('/')

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    return render_template('view_recipe.html', recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))
    
if __name__ == '__main__':
    if __name__ == '__main__':
        # app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True, threaded=True)
        app.run(debug=True, threaded=True)