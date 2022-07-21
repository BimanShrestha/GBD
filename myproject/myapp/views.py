import json
from django.shortcuts import render, redirect
from .models import detail
from django.http import HttpResponse
from datetime import datetime


def index(request):
    if request.method == 'POST':
        data = (request.FILES['json'])
        readjson = json.load(data)
        print(readjson)
        # content=readjson['main_content']
        # print(content)
        for i in readjson['main_content']:
            for da in i['content']:
                data = detail(scheme=readjson['name'], mainxpath=i['main_xpath'], category=i['category'],
                              xapth=da['xpath'], field=da['field'],
                              created_at=datetime.now(), updated_at=datetime.now())
                data.save()

        # return HttpResponse("file uploaded successfuly")
    return render(request, "index.html")

def project(request):
    context = {}
    name = detail.objects.values_list('scheme',flat=True).distinct()
    # print(name)
    context['name'] = name
    print(context)
    return render(request, 'detail.html', context)

def view(request):
    context={}
    name =detail.objects.values_list('scheme',flat=True).distinct()
    category=detail.objects.values_list('category',flat=True).distinct()
    mainxpath =detail.objects.values_list('mainxpath',flat=True).distinct()
    context['name'] = name
    context['main_xpath'] = mainxpath
    context['category'] = category
    return render(request,'view.html',context)

def myview(request):
    detail_list =detail.objects.all().order_by('category','field')
    if request.method == 'POST':
        uploaded_xpath = request.POST.get("new_xpath")
        xpath = request.POST.get('new_xpath')
        id = request.POST.get('database_id')
        det = detail.objects.get(pk=id)
        det.xapth = xpath
        det.save()
        print(uploaded_xpath)




    return render(request,'edit.html',
                  {'detail_list':detail_list})

# def project(request):
#     return render(request, 'detail.html')
def update(request):
    details=detail.objects.all()
    return render(request,'update.html',
    {'details':details})
# def getdata(request):
#     details=detail.object.get()
#    return render(request)
def detailview(request):
    detail_list=detail.objects.all()
    return render(request,'individual_detail.html',{'detail_list':detail_list})

def show_detail(request,detail_id): 
    details=detail.object.get(pk=detail_id)
    return render(request,'single_html',{'details:details'})

def csv_upload(request):
    if request.method == 'POST':
        data = (request.FILES['csv'])
        readjson = json.load(data)
        print(readjson)
        return render(request, "csv.html")

def xpathedit(request):
    context = {}
    mainxpath = detail.objects.values_list('mainxpath', flat=True).distinct()
    context['main_xpath'] = mainxpath
    return render(request, 'my.html', context)

