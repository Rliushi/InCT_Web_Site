from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.


def index(request):
    return HttpResponse(u'Hello World')


def test(request):
    return render(request, 'HiMath7_1.html')


def getimages(request):
        section_id = request.GET['section']
        curr_dir = os.path.dirname(os.path.dirname(__file__))
        image_dir = os.path.join(curr_dir, 'ClassQuery', 'static', 'images', section_id)
        count = len(os.listdir(image_dir))
        image_info = list()
        for i in range(count):
            image_info.append("static/images/" + section_id + "/" + section_id.replace("section_", "") + "-" + str(i + 1) + ".png")
        return render(request, 'HiMath7_1.html', {'image_info': image_info})

