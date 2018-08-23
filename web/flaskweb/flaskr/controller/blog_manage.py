from flaskr.model.User import User
from flaskr.model.Category import Category
from flask_login import login_required, login_user, logout_user
from flaskr import app, db
from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g
from werkzeug.utils import secure_filename


@app.route('/')
@login_required
def show_entries():
    categories = Category.query.all()
    return render_template('show_entries.html', entries=categories)


@app.route('/add', methods=['POST'])
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = db.session.query(User).filter_by(username=request.form['username']).first()
        if user is None:
            flash('用户不存在')
        elif user.password is not request.form['password']:
            flash('密码错误')
        else:
            login_user(user)
            flash('登录成功')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/user/<username>') # 接收string
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>') #接收int
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/postf/<float:post_id>') # 接收float
def show_post_f(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>') # 接收路径，与string类似，可以包含斜杠
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f = request.files['the_file']
        f.save('./uploads/'+secure_filename(f.filename))
