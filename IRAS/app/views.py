from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect # 可进行重定向，自行学习
from django.urls import reverse
# 视图函数
# Create your views here.
def index(request):# 接受request
    context = {'words':'hello'}#传递上下文
    return render(request,'app/index.html',context)
    # 进行渲染
#
#
#
#