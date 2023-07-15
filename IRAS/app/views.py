from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect # 可进行重定向，自行学习
from django.urls import reverse
from .forms import UploadFileForm
from tempfile import TemporaryFile
# 视图函数
# Create your views here.
def index(request):# 接受request
    context = {'words':'hello'}#传递上下文
    return render(request,'app/index.html',context)
def multivis(request):
    return render(request,'app/multi-vis.html')
def sf(request):
    return render(request,'app/single-result-fig.html')
def sv(request):
    return render(request,'app/single-result-vis.html')
def sr(request):
    return render(request,'app/single-result-res.html')
def single(request):
    return render(request,'app/single.html')
def singleres(request):
    return render(request,'app/single-result.html')
def multiply(request):
    return render(request,'app/multiply.html')
def multires(request):
    return render(request,'app/multi-result.html')
def multimatch(request):
    return render(request,'app/multi-match.html')
def multiupres(request):
    return render(request,'app/multi-upload-resume.html')
def multiuppos(request):
    return render(request,'app/multi-upload-position.html')

#进行文件处理
import os
def handle_uploaded_file(file,filename):
    type = filename.split('.')[-1]
    
def singleupload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"],request.POST.get("title"))
            return HttpResponseRedirect(reverse('app:singleres'))
    else:
        form = UploadFileForm()
    return render(request, "app/single.html", {"form": form})