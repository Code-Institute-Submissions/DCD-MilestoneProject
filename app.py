import os
from flask import Flask, redirect, render_template, request, url_for, session, flash
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FieldList
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS_IS_SECRET_KEY' 
app.config['MONGO_DBNAME'] = 'dcd-milestone'
app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds243041.mlab.com:43041/dcd-milestone'

mongo = PyMongo(app)

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
    return str(request.form.to_dict())
    
if __name__ == '__main__':
    if __name__ == '__main__':
        app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True, threaded=True)