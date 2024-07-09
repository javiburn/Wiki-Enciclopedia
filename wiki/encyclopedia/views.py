from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from . import util

# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html")

def test(request):
    return HttpResponseNotFound()

def search(request, name):
    return HttpResponse(util.get_entry(name))