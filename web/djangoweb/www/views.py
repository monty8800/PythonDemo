from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render
from www import models


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 添加数据到数据库
        models.UserInfo.objects.create(username=username, password=password)

        print(username, password)

    # 查询UserInfo表中所有数据
    user_list = models.UserInfo.objects.all().order_by('-id')  # order_by排序 - 表示倒序 id 为字段名，order_by('-id')表示按id倒序排列
    # return HttpResponse('Hello Monty')
    return render(request, 'index.html', {'data': user_list})
