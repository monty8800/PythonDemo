from django.contrib import admin

# Register your models here.

from .models import Luhuo

class LuhuoAdmin(admin.ModelAdmin):
    list_display = ['product','add_time', 'platform', 'order_num', 'num', 'price','money','gather']
    search_fields = ['add_time', 'platform', 'order_num', 'product']
    list_filter = ['add_time', 'platform', 'product']

admin.site.register(Luhuo,LuhuoAdmin)
