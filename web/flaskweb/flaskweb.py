from flask import Flask, url_for, request,flash, render_template, redirect, abort
from flaskr.forms import LoginForm
from flaskr.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')  # http://127.0.0.1:8081
def hello_world():
    # return 'Hello World!'
    user_agent = request.headers.get('User_Agent')
    return user_agent
    # return redirect(url_for('login'))


@app.route('/index')  # http://127.0.0.1:8081/index
def index():
    user = {
        'username': 'Monty'
    }
    posts = [
        {
            'author': {'username':'Monty'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }

    ]
    return render_template('index.html', title='Index', user=user,posts=posts)


@app.route('/var/<username>')  # http://127.0.0.1:8081/var/monty 传入变量
def variable(username):
    return 'value is %s' % username


@app.route('/var/<int:age>')  # http://127.0.0.1:8081/var/11 接收int类型数据
def varInt(age):
    return 'age is %s' % age


@app.route('/projects/')  # 访问/projects会被重定向到/projects/
def projects():
    return 'The project page'


@app.route('/about')  # 访问/about正常，访问/about/报404
def about():
    return 'The about page'


# 动态构造url，暂时不能用，原因未知
# with app.test_request_context():
#     print(url_for('category'))
#     print(url_for('login'))
#     print(url_for('login', next('/')))
#     print(url_for('profile', username='monty'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {} , remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
    # app.run(port=8081, debug=True)  # port指定端口，debug指定是否调试模式


