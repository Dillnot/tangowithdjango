from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!<a href ='/rango/about'>about</a>")

def about(request):
    return HttpResponse("<p>rango says here is the about page</p><p> this has been put together by dylan stevenson ,2082487S</p><a href ='/rango/'>index</a>")
