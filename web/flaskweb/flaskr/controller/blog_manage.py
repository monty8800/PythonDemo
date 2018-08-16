
from flaskr.model.User import User
from flaskr.model.Category import Category
from flask_login import login_required,login_user,logout_user
from flaskr import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g

@app.route('/')
@login_required
def show_entries():
    categories = Category.query.all()
    return render_template('show_entries.html',entries=categories)

@app.route('/add',methods=['POST'])
@login_required
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    title = request.form['title']
    content = request.form['content']
    category = request.form['category']
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = db.session.query(User).filter_by(username=request.form['username']).first()
        if user is None:
            flash('user is none')
        else:
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_entries'))
