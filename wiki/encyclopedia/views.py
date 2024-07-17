from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from . import util
import markdown2
import glob

# Create your views here.
def index(request):
    path = "./entries"
    entries_md = glob.glob1(path, "*.md")
    entries = [ent[: -3].title() for ent in entries_md]
    if request.method == "POST":
        name = request.POST['q']
        try:
            html = markdown2.markdown(util.get_entry(name))
        except:
            entries_md = glob.glob1(path, f"*{name}*.md")
            entries = [ent[: -3].title() for ent in entries_md]
            return render(request, "encyclopedia/search.html", {
                "entries": entries,
            })
        return render(request, "encyclopedia/entry.html", {
            "name": util.get_entry(name).title(), \
            "content": html
        })
    else:
         return render(request, "encyclopedia/index.html", {
             "entries": entries
         })

def test(request):
    return HttpResponseNotFound()

def search_by_url(request, name):
    name = name.lower()
    try:
        html = markdown2.markdown(util.get_entry(name))
    except:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    return render(request, "encyclopedia/entry.html", {
            "name": name.title(), \
            "content": html
        })