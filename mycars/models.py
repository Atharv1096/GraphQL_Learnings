# cookbook/ingredients/models.py
from django.db import models


class Build(models.Model):
    name = models.CharField(max_length=100)
    differentiating_factor = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    mileage = models.IntegerField()
    description = models.CharField(max_length = 500)
    build = models.ForeignKey(
        Build, related_name="mycars", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, related_name="mycars", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
