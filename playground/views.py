from django.shortcuts import render
from django.http import HttpResponse


def cal():
    x = 1
    y = 2
    return x


# Create your views here.
def say_hello(request):
    x = cal()
    y = 2
    return render(request, "hello.html", {"name": "Phong"})
