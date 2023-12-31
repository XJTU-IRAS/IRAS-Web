from django.shortcuts import render
from django.http import  HttpResponseRedirect # 可进行重定向，自行学习
from django.urls import reverse
from .forms import IntervieweeForm, UploadFileForm
from .handles import  handle_uploaded_file
from .models import Interviewee,Position
# 视图函数
# Create your views here.
def index(request):# 接受request
    context = {'words':'hello'}#传递上下文
    return render(request,'app/index.html',context)
def multivis(request):
    return render(request,'app/multi-vis.html')
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
def multiupload(request):
    return render(request, 'app/multi-upload-resume.html')
def multiuppos(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        text = request.POST.get('text')
        #两种输入时，优先选择text
        if text !="":
            itv = ()
            itv.origin_text=text
            itv.file_name="default"
            itv.save()
            return HttpResponseRedirect(reverse('app:multiuppos'))
        else:
            if form.is_valid():
                itv = Position()
                itv.origin_text=handle_uploaded_file(request.FILES['file'],request.POST.get('title'))
                itv.file_name=request.POST.get('title')
                itv.save()
                return HttpResponseRedirect(reverse('app:multiuppos'))
            else :
                return render(request, "app/multi-upload-position.html")
    else:
        form = UploadFileForm()
        return render(request, "app/multi-upload-position.html")   
def singleupload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        text = request.POST.get('text')
        #两种输入时，优先选择text
        if text !="":
            itv = Interviewee()
            itv.origin_text=text
            itv.file_name="default"
            itv.save()
            return HttpResponseRedirect(reverse('app:singleres',args=[itv.id]))
        else:
            if form.is_valid():
                itv = Interviewee()
                itv.origin_text=handle_uploaded_file(request.FILES['file'],request.POST.get('title'))
                itv.file_name=request.POST.get('title')
                itv.save()
                return HttpResponseRedirect(reverse('app:singleres',args=[itv.id]))
            else :
                return render(request, "app/single.html")
    else:
        form = UploadFileForm()
        return render(request, "app/single.html")
def singleres(request,itv_id):
    context = {'id': itv_id}
    return render(request,'app/single-result.html',context)   
def sf(request):
    return render(request,'app/single-result-fig.html')
def sv(request):
    return render(request,'app/single-result-vis.html')
def sr(request):
    id = request.GET.get('id')
    itv=Interviewee.objects.get(id=id)
    form = IntervieweeForm(instance=itv)
    context = {'form':form}
    return render(request,'app/single-result-res.html',context)
def single(request):
    return render(request,'app/single.html')
