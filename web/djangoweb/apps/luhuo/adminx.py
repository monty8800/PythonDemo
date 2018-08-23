__author__ = 'Monty'
__date__ = '2018/8/23 下午3:06'


import xadmin
from .models import Luhuo

class LuhuoAdmin(object):
    list_display = ['product','add_time', 'platform', 'order_num', 'num', 'price','money','gather']
    search_fields = ['add_time', 'platform', 'order_num', 'product']
    list_filter = ['add_time', 'platform', 'order_num', 'product']

xadmin.site.register(Luhuo,LuhuoAdmin)