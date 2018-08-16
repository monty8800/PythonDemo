from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager


#创建项目对象
app = Flask(__name__)
#加载配置文件内容
app.config.from_object('flaskr.setting') #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS') #环境变量，指向配置文件setting的路径

#创建数据库对象
db = SQLAlchemy(app)

from flaskr.model import User,Category

from flaskr.controller import blog_manage

login_manager = LoginManager()
login_manager.init_app(app)
print(login_manager)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User.User).filter_by(id=user_id).first()
