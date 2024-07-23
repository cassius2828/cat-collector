from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

# View functions are like controller function
# they process http requests

from .models import Cat


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    # 'cats' would be the variable name (cat) in the cats/index.html
    cats = Cat.objects.all()  # using model to select all the rows in the cats table
    return render(request, "cats/index.html", {"cats": cats})


# cat_id comes from the param name in urls.py
def cat_details(request, cat_id):
    # no need for async await bc python is synchronous
    cat = Cat.objects.get(id=cat_id)
    return render(request, "cats/details.html", {"cat": cat})


class CatCreate(CreateView):
    model = Cat
    fields = "__all__"  # referencing the model fields
    # how to define a redirect
    # * absolute url
    # success_url = '/cats/'


class CatUpdate(UpdateView):
    model = Cat
    # disallow the updating of the cat's name
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    # since we just deleted the resource, we have to go to the index now
    # so we need to put the abs url here
    success_url = '/cats/'


# temporary data until we config our models


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# cats = [
#     Cat("Dobbie", "Sphinx", "Loves treats", 3),
#     Cat("bear", "Sphinx", "Loves fighting", 9),
#     Cat("taco", "Sphinx", "Loves lindsey", 3),
#     Cat("smudge", "Tiger", "Loves luna", 0),
# ]
