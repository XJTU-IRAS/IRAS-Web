from django.urls import path
from . import views
urlpatterns=[
    path(r'',views.index,name='index'),
    # 当url匹配到参数1时，调用views模块的index函数进行request处理
]