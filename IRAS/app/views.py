from django.shortcuts import render
from django.http import  HttpResponseRedirect # 可进行重定向，自行学习
from django.urls import reverse

from .info_extract import info_extract
from .forms import IntervieweeForm, UploadFileForm
from .handles import  handle_uploaded_file
from .models import Experience, Interviewee,Position
from .dbcon import gender_group,education_group,year_group
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
    start = request.GET.get('start')
    end = request.GET.get('end')
    context = {'chardata':education_group(start,end)}
    return render(request,'app/multi-result.html',context)
def multimatch(request):
    return render(request,'app/multi-match.html')
def multiupres(request):
    return render(request,'app/multi-upload-resume.html')
def multiuppos(request):
    return render(request,'app/multi-upload-position.html')
#进行多简历上传处理
def multiupload(request):
    files = request.FILES.getlist('files')
    end_id = 0
    for f in files:
        itv = Interviewee()
        itv.origin_text=handle_uploaded_file(f,f.name)
        itv.name=f.name
        info = info_extract(itv.origin_text)
        if 'name' in info.keys():
            itv.name = info['name']
        if 'sex' in info.keys():
            itv.gender = info['sex']
        if 'age' in info.keys():
            itv.age = info['age']
        if 'education' in info.keys():
            itv.education = info['education']
        if 'school' in info.keys():
            itv.school = info['school']
        if 'work_time' in info.keys():
            itv.work_years=info['work_time']
        if 'job_intention' in info.keys():
            itv.ideal_pos=info['job_intention']
        itv.save()
                
        experience = info['work_experience']
        for e in experience:
            exp = Experience()
            exp.interviewee = itv
            if 'section' in e.keys():
                exp.name = e['section']
            if 'company' in e.keys():
                exp.company = e['company']
            if 'job' in e.keys():
                exp.info = e['job']
            exp.save()
        end_id = itv.id
    context={"start":end_id-len(files)+1,"end":end_id}
    return render(request, 'app/multi-upload-resume.html',context)

def multiuppos(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        text = request.POST.get('text')
        #两种输入时，优先选择text
        if text !="":
            pos = Position()
            pos.origin_text=text
            pos.file_name="default"
            pos.save()
            return HttpResponseRedirect(reverse('app:multiupres'))
        else:
            if form.is_valid():
                pos= Position()
                pos.origin_text=handle_uploaded_file(request.FILES['file'],request.POST.get('title'))
                pos.file_name=request.POST.get('title')
                pos.save()
                return HttpResponseRedirect(reverse('app:multiupres'))
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
                info = info_extract(itv.origin_text)
                if 'name' in info.keys():
                    itv.name = info['name']
                if 'age' in info.keys():
                    itv.age = info['age']
                if 'sex' in info.keys():
                    itv.gender = info['sex']
                if 'education' in info.keys():
                    itv.education = info['education']
                if 'school' in info.keys():
                    itv.school = info['school']
                if 'work_time' in info.keys():
                    itv.work_years=info['work_time']
                if 'job_intention' in info.keys():
                    itv.ideal_pos=info['job_intention']
                itv.save()
                
                experience = info['work_experience']
                for e in experience:
                    exp = Experience()
                    exp.interviewee = itv
                    if 'section' in e.keys():
                        exp.name = e['section']
                    if 'company' in e.keys():
                        exp.company = e['company']
                    if 'job' in e.keys():
                        exp.info = e['job']
                    exp.save()
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
from .figures import generate_cloud
def sv(request):
    id = request.GET.get('id')
    itv=Interviewee.objects.get(id=id)
    url = generate_cloud(itv.origin_text)
    context = {"url":url}
    return render(request,'app/single-result-vis.html',context)
# 单简历解析结果
def sr(request):
    id = request.GET.get('id')
    itv=Interviewee.objects.get(id=id)
    form = IntervieweeForm(instance=itv)
    context = {'form':form}
    return render(request,'app/single-result-res.html',context)

def single(request):
    return render(request,'app/single.html')
