from datetime import datetime
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pull_category'

    def __str__(self):
        return self.name


class GenericPull(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    details = models.TextField()
    category = models.ManyToManyField(Categories)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pull_generic'

    def __str__(self):
        return self.name


class SpecificPull(models.Model):
    generic_pull = models.ForeignKey(GenericPull,
                                     on_delete=models.CASCADE,
                                     related_name='generic_pull')
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    class Meta:
        db_table = 'pull_specific'

    def __str__(self):
        return self.name


class Colors(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'pull_color'

    def __str__(self):
        return self.name


class PullImage(models.Model):
    image = models.TextField()
    order = models.BooleanField(default=False)
    class Meta:
        db_table = 'pull_image'
