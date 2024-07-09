from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html")

def test(request):
    return HttpResponseNotFound()