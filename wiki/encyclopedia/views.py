from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from . import util
import markdown2

# Create your views here.

def index(request):
    return render(request, "encyclopedia/index.html")

def test(request):
    return HttpResponseNotFound()

def search(request, name):
    try:
        html = markdown2.markdown(util.get_entry(name))
    except:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    return HttpResponse(html)