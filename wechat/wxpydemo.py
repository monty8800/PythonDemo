# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
wangyang = bot.friends.search('wangyang')
print(wangyang)
bot.add_friend(wangyang,verify_content='来自通讯录的朋友')