__author__ = 'Monty'
__date__ = '2018/8/23 上午11:33'

import xadmin
from .models import EmailVerifyRecord
from .models import Banner
from xadmin import views

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)

class BaseSetting(object):
    enable_themes = True  # 将隐藏的主题属性显现
    use_bootswatch = True  # 设置后才有很多主题可用</code>

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = "Monty后台"
    site_footer = "Monty后台"
    menu_style = "accordion"  # 将各app的model折叠起来


xadmin.site.register(views.CommAdminView, GlobalSettings)  # 注册全局设定
