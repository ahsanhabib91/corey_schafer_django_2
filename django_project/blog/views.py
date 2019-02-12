from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>This is Blog home page</h2>')


def about(request):
    return HttpResponse('<h1>This is Blog about page</h2>')
