DEBUG = True


SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flask:123456@132.232.104.62:3306/flask?charset=utf8"