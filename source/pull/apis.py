from django.conf.urls import url
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie.authentication import  ApiKeyAuthentication, Authentication
from tastypie.exceptions import BadRequest
from tastypie import fields
from .models import (Categories,
                     GenericPull,
                     Colors,
                     SpecificPull,
                     PullModel,
                     PullUrl)
from  ..account.apis import UserResource


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


class PullModelResource(ModelResource):
    class Meta:
        queryset = PullModel.objects.all()
        resource_name = 'pull'
        include_resource_uri = False
        authentication = Authentication()
        authorization = Authorization()


class PullUrlResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    class Meta:
        queryset = PullUrl.objects.all()
        resource_name = 'pulls/user'
        filtering = {
            'slug': ALL,
            'user': ALL,
        }
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>[\w\d_.-]+)/$" %
                (self._meta.resource_name),
                self.wrap_view('user_pull'), name="api_user_pull"),
        ]

    def user_pull(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        try:
            user_id = request.resolver_match.kwargs["pk"]
            user = User.objects.get(id=user_id)
        except KeyError:
            return BadRequest('Cannot find this user')
        return PullUrlResource().get_list(request, user=user)

    def dehydrate(self, bundle):
        bundle.data["user"] = {"id":bundle.obj.user.id,
                               "username":bundle.obj.user.username
                              }
        return super(PullUrlResource, self).dehydrate(bundle)

    def obj_create(self, bundle, **kwargs):
        try:
            return super(PullUrlResource, self).obj_create(bundle, user=bundle.request.user)
        except Exception:
            raise BadRequest("Create URL false")
