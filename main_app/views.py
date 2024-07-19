from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View functions are like controller function
# they process http requests

# temporary data until we config our models


class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


cats = [
    Cat("Dobbie", "Sphinx", "Loves treats", 3),
    Cat("bear", "Sphinx", "Loves fighting", 9),
    Cat("taco", "Sphinx", "Loves lindsey", 3),
    Cat("smudge", "Tiger", "Loves luna", 0),
]


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    # 'cats' would be the variable name (cat) in the cats/index.html
    return render(request, "cats/index.html", {"cats": cats})
