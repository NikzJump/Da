from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=99)


class Warehouse(models.Model):
    titles = models.ManyToManyField(Product)


class Group(models.Model):
    titles = models.ManyToManyField(Product)
