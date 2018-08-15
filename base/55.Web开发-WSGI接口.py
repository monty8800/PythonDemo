
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：
# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text-html')]) # 发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
#     return [b'<h1>Hello, web!</h1>']

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
#
# environ：一个包含所有HTTP请求信息的dict对象；
#
# start_response：一个发送HTTP响应的函数。


# 运行WSGI服务

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

