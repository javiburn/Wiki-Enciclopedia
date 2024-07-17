from . import views
from django.urls import path

appname = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.search_by_url, name="search_url"),
]