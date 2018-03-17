from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse(u'Hello World')


def test(request):
    return render(request, 'HiMath7_1.html')
