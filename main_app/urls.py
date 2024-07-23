from django.urls import path

from . import (
    views,
)  # import all funcs in views file and attach them to the object views

urlpatterns = [
    #    use trailing slashes and a root route is a blank string
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cats/", views.cat_index, name="cat_index"),
    # ? everytime we get a http req, it looks at params and grabs the splat of the id
    # preferace the id with the resource
    path("cats/<int:cat_id>/", views.cat_details, name="cat_details"),
    # as_view initializes ... ?
    path("cats/create/", views.CatCreate.as_view(), name="cat_create"),
    # class based views expect params to be named "pk" (primary key)
    path("cats/<int:pk>/update/", views.CatUpdate.as_view(), name="cat-update"),
    path("cats/<int:pk>/delete/", views.CatDelete.as_view(), name="cat-delete"),
]
