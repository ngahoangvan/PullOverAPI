from django.conf.urls import url
# from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie.authentication import  ApiKeyAuthentication, Authentication
# from tastypie.exceptions import BadRequest
from tastypie import fields
from .models import (Categories,
                     GenericPull,
                     Colors,
                     SpecificPull)


class CategoriesResource(ModelResource):
    class Meta:
        queryset = Categories.objects.all()
        resource_name = 'categories'
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = Authorization()


class GenericPullResource(ModelResource):
    class Meta:
        queryset = GenericPull.objects.all()
        resource_name = 'generic-pull'
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = Authorization()


class SpecificPullResource(ModelResource):
    class Meta:
        queryset = SpecificPull.objects.all()
        resource_name = 'specific-pull'
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = Authorization()


class ColorsResource(ModelResource):
    class Meta:
        queryset = Colors.objects.all()
        resource_name = 'colors'
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
