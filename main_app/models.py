from django.db import models
from django.urls import reverse


# Create your models here.
# we are inheriting the necessary methods from django premade classes
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# absolute redirect in class
    def get_absolute_url(self):
        return reverse("cat_details", kwargs={"cat_id": self.id})
