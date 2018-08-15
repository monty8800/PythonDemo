# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

# 1.纯文本邮件：
# from email.mime.text import MIMEText
# msg = MIMEText('Hello,Send by Python...','plain','utf-8') # 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# # 1.1 通过SMTP发送出去
#
# # 输入Email地址和口令
# from_addr = input('From:')
# password = input('Password:') # hkgwgufkuwftbfad
#
# # 输入收件人地址:
# to_addr = input('To:')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP Server:')
#
# import smtplib
# server = smtplib.SMTP(smtp_server,25)# smtp默认端口是25
# server.set_debuglevel(1) # set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
# server.login(from_addr,password) # login()方法用来登录SMTP服务器
# server.sendmail(from_addr,[to_addr],msg.as_string()) # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
# server.quit()

# 2.优化邮件内容
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
#
# import smtplib
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = input('From: ')
# password = input('Password: ') # hkgwgufkuwftbfad
# to_addr = input('To: ') # 1002908397@qq.com 182191788830@163.com
# # smtp_server = input('SMTP server: ')
# smtp_server = 'smtp.qq.com'
# print('smtp_server:',smtp_server)
#
# # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') # 发送文本邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://mwu.me">mwu.me</a>...</p>' +
#     '</body></html>', 'html', 'utf-8') # 发送html邮件
# msg['From'] = _format_addr('Monty <%s>' % from_addr) # 发件人
# msg['To'] = _format_addr('管理员 <%s>' % to_addr) # 收件人
# msg['Subject'] = Header('来自Monty的问候……', 'utf-8').encode() # 标题
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# 3.发送HTML邮件
# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：

# 4.发送附件
# 构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From: ')
password = input('Password: ')  # hkgwgufkuwftbfad
to_addr = input('To: ')  # 18219178830@163.com
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.qq.com'
print('smtp_server:', smtp_server)

if not password:
    password = 'hkgwgufkuwftbfad'
    print('password',password)

if not to_addr:
    to_addr = '18219178830@163.com'
    print('To:',to_addr)

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') # 发送文本邮件
msg = MIMEMultipart()  # 发送带附件的邮件
msg['From'] = _format_addr('Monty <%s>' % from_addr)  # 发件人
msg['To'] = _format_addr('管理员 <%s>' % to_addr)  # 收件人
msg['Subject'] = Header('来自Monty的问候……', 'utf-8').encode()  # 标题

# 邮件正文是MIMEText，将图片放入正文 src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
msg.attach(MIMEText('<html><body><h1>Hello,大力</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '<p>send by <a href="http://mwu.me">mwu.me</a>...</p>' +
                    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('./demo/files/usr.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='monty.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='monty.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.starttls() # 创建安全连接，加密smtp
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

exit()
# 5.同时发送文本和html
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# # 正常发送msg对象...

# 6.加密smtp
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
#
# 某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
#
# 必须知道，Gmail的SMTP端口是587，因此，修改代码如下：
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()
# # 剩下的代码和前面的一模一样:
# server.set_debuglevel(1)
# ...
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样。
#
# 如果因为网络问题无法连接Gmail的SMTP服务器，请相信我们的代码是没有问题的，你需要对你的网络设置做必要的调整。