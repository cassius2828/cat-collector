from django.urls import path

from . import (
    views,
)  # import all funcs in views file and attach them to the object views

urlpatterns = [
    #    use trailing slashes and a root route is a blank string
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('cats/', views.cat_index, name="cat_index"),
]
