from django.urls import path
from . import views
urlpatterns=[
    path(r'',views.index,name='index'),
    # 当url匹配到参数1时，调用views模块的index函数进行request处理
    path(r'single-result-fig',views.sf,name='sf'),
    path(r'single-result-res',views.sr,name='sr'),
    path(r'single-result-vis',views.sv,name='sv'),
    path(r'single-result',views.singleres,name='singleres'),
    path(r'single',views.single,name='single'),
    path(r'multi-result',views.multires,name='multires'),
    path(r'multi-match',views.multimatch,name='multimatch'),
    path(r'multi-vis',views.multivis,name='multivis'),
    path(r'multi-upload-resume',views.multiupres,name='multiupres'),
    path(r'multi-upload-position',views.multiuppos,name='multiuppos'),
    path(r'multiply',views.multiply,name='multiply'),
]