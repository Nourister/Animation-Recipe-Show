from flask import current_app as app, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.forms import LoginForm,RegistrationForm, ContactForm
from app.models import User, Recipe
from flask import render_template, redirect, url_for, request


recipes = [
    {
        'name': 'Chicken Tikka Masala',
        'ingredients': [
            {'name': 'plain yogurt', 'quantity': '1 cup'},
            {'name': 'lemon juice', 'quantity': '1 tablespoon'},
            {'name': 'ground cumin', 'quantity': '2 teaspoons'},
            {'name': 'ground cinnamon', 'quantity': '1 teaspoon'},
            {'name': 'cayenne pepper', 'quantity': '2 teaspoons'},
            {'name': 'freshly ground black pepper', 'quantity': '2 teaspoons'},
            {'name': 'minced fresh ginger', 'quantity': '1 tablespoon'},
            {'name': 'salt', 'quantity': '1 teaspoon'},
            {'name': 'boneless skinless chicken breasts', 'quantity': '3, cut into bite-sized pieces'},
            {'name': 'butter', 'quantity': '1 tablespoon'},
            {'name': 'garlic', 'quantity': '1 clove, minced'},
            {'name': 'jalapeno pepper', 'quantity': '1, finely chopped'},
            {'name': 'paprika', 'quantity': '2 teaspoons'},
            {'name': 'tomato sauce', 'quantity': '1 (8 ounce) can'},
            {'name': 'heavy cream', 'quantity': '1 cup'},
            {'name': 'fresh cilantro leaves', 'quantity': 'optional, chopped'},
        ],
        'instructions': [
            'In a large bowl, combine yogurt, lemon juice, cumin, cinnamon, cayenne, black pepper, ginger, and salt.',
            'Add chicken, and stir to coat. Cover and refrigerate for 1 hour.',
            'Preheat a grill for high heat.',
            'Thread chicken onto skewers, and discard marinade.',
            'Grill until juices run clear, about 5 minutes on each side.',
            'Melt butter in a large heavy skillet over medium heat. Sauté garlic and jalapeno for 1 minute.',
            'Season with cumin, paprika, and salt. Stir in tomato sauce and cream.',
            'Simmer on low heat until sauce thickens, about 20 minutes.',
            'Add grilled chicken, and simmer for 10 minutes.',
            'Garnish with fresh cilantro and serve.'
        ],
        'preparation_time': '1 hour 30 minutes',
        'cooking_time': '45 minutes',
        'servings': '4'
    },
    {
        'name': 'Spaghetti Carbonara',
        'ingredients': [
            {'name': 'spaghetti', 'quantity': '12 ounces'},
            {'name': 'olive oil', 'quantity': '1 tablespoon'},
            {'name': 'pancetta', 'quantity': '4 ounces, diced'},
            {'name': 'garlic', 'quantity': '2 cloves, minced'},
            {'name': 'eggs', 'quantity': '2 large'},
            {'name': 'grated Parmesan cheese', 'quantity': '1 cup'},
            {'name': 'black pepper', 'quantity': 'to taste'},
            {'name': 'salt', 'quantity': 'to taste'},
            {'name': 'fresh parsley', 'quantity': 'optional, chopped'},
        ],
        'instructions': [
            'Cook spaghetti according to package instructions. Reserve 1 cup of pasta water and drain the rest.',
            'Heat olive oil in a large skillet over medium heat. Add pancetta and cook until crispy.',
            'Add garlic to the skillet and cook for 1 minute.',
            'In a bowl, whisk together eggs and Parmesan cheese.',
            'Add cooked spaghetti to the skillet with pancetta and garlic. Remove from heat.',
            'Quickly pour egg and cheese mixture over pasta, stirring rapidly to create a creamy sauce.',
            'If the sauce is too thick, add reserved pasta water a little at a time until desired consistency is reached.',
            'Season with black pepper and salt to taste.',
            'Garnish with fresh parsley and serve immediately.'
        ],
        'preparation_time': '10 minutes',
        'cooking_time': '20 minutes',
        'servings': '4'
    },
    {
        'name': 'Beef Stroganoff',
        'ingredients': [
            {'name': 'egg noodles', 'quantity': '8 ounces'},
            {'name': 'olive oil', 'quantity': '1 tablespoon'},
            {'name': 'beef sirloin', 'quantity': '1 pound, cut into strips'},
            {'name': 'onion', 'quantity': '1, diced'},
            {'name': 'mushrooms', 'quantity': '8 ounces, sliced'},
            {'name': 'garlic', 'quantity': '2 cloves, minced'},
            {'name': 'beef broth', 'quantity': '1 cup'},
            {'name': 'sour cream', 'quantity': '1 cup'},
            {'name': 'Dijon mustard', 'quantity': '1 tablespoon'},
            {'name': 'salt', 'quantity': 'to taste'},
            {'name': 'black pepper', 'quantity': 'to taste'},
            {'name': 'fresh parsley', 'quantity': 'optional, chopped'},
        ],
        'instructions': [
            'Cook egg noodles according to package instructions. Drain and set aside.',
            'Heat olive oil in a large skillet over medium-high heat. Add beef strips and cook until browned. Remove beef from skillet and set aside.',
            'Add onion and mushrooms to the skillet and cook until tender, about 5 minutes.',
            'Add garlic and cook for another minute.',
            'Return beef to the skillet. Stir in beef broth and bring to a simmer.',
            'Reduce heat to low and stir in sour cream and Dijon mustard. Cook until heated through, about 2 minutes.',
            'Season with salt and black pepper to taste.',
            'Serve over egg noodles and garnish with fresh parsley.'
        ],
        'preparation_time': '15 minutes',
        'cooking_time': '25 minutes',
        'servings': '4'
    }
]


@app.route("/")
def index():
    return render_template("index.html", recipes=recipes)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/recipes')
def recipes_list():
    recipes_list = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes_list)

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Handle form submission (e.g., send an email or save to the database)
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = User.hash_password(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))