from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


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
    class Meta:
        db_table = 'pull_image'


class PullModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.TextField()
    class Meta:
        db_table = 'pull_model'


class PullUrl(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user')
    url = models.TextField()
    class Meta:
        db_table = 'pull_url'
        