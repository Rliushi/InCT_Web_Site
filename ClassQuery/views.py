from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import ClassImage
from .models import XjhInfo
from django.core import serializers
import json
from django.http import JsonResponse
# Create your views here.


def index(request):
    return HttpResponse(u'Hello World')


def test(request):
    return render(request, 'ClassQuery/HiMath7_1.html')


def xjh(request):
    return render(request, 'ClassQuery/XJH.html')

# def getimages(request):
#         section_id = request.GET['section']
#         curr_dir = os.path.dirname(os.path.dirname(__file__))
#         image_dir = os.path.join(curr_dir, 'ClassQuery', 'static', 'images', section_id)
#         count = len(os.listdir(image_dir))
#         image_info = list()
#         for i in range(count):
#             image_info.append("static/images/" + section_id + "/" + section_id.replace("section_", "") + "-" + str(i + 1) + ".png")
#         return render(request, 'ClassQuery/HiMath7_1.html', {'image_info': image_info})


def getimages(request):
    section_id = request.GET['section']
    class_name = request.GET['class']
    image_info = ClassImage.objects.filter(className=class_name).filter(sectionID=section_id).order_by('imageSeq')

    return render(request, 'ClassQuery/HiMath7_1.html', {'image_info': image_info})


def xjh_query(request):
    city_name = request.GET['city']
    school_engname_t = request.GET['school']
    # school_name = request.GET['school']
    xjh_info = XjhInfo.objects.filter(city_id=city_name).filter(school_engname=school_engname_t)
    tmp_list = []
    for item in xjh_info:
        tmp_dict = dict()
        tmp_dict['city'] = item.city
        tmp_dict['school'] = item.school
        tmp_dict['company'] = item.company
        tmp_dict['location'] = item.location
        tmp_dict['time'] = item.time[:4] + '-' + item.time[4:6] + '-' + item.time[6:8] + ' ' + item.time[8:10] + ':' + item.time[10:12] + ':' + item.time[12:14]
        tmp_list.append(tmp_dict)
    # data = serializers.serialize('json', xjh_info, ensure_ascii=False)
    # data = json.dumps(tmp_list, ensure_ascii=False)
    return JsonResponse(tmp_list, safe=False)
    # return HttpResponse(data, content_type='application/json', charset='utf-8')

def get_school(request):
    city_id_t = request.GET['city']
    school_info = XjhInfo.objects.filter(city_id=city_id_t).values('school', 'school_engname').distinct()
    tmp_list = []
    for item in school_info:
        tmp_dict = dict()
        tmp_dict['school'] = item['school']
        tmp_dict['school_engname'] = item['school_engname']
        tmp_list.append(tmp_dict)

    return JsonResponse(tmp_list, safe=False)

