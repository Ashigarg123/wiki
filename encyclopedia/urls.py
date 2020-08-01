from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("css/", views.CSS, name="css")
    path("Create", views.Create, name="create"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("Edit/<str:title>", views.EditPage,name="edit"),
    path("EditPage", views.EditPage,name="edit" ),
    path("random/", views.random_page, name="random")
]
