from django.contrib import admin

# Register your models here.
from .models import Cat
admin.site.register(Cat) # creates a crud app for this model for our admins