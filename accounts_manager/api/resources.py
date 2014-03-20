from django.conf import settings
from tastypie import fields
from tastypie.authentication import MultiAuthentication, BasicAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.fields import ToManyField, CharField, ToOneField
from tastypie.resources import ModelResource, Resource
from accounts_manager.models import ActorProfile, Tag, ProductionProfile
from auditioneer.models import Audition, Part


class ActorResource(ModelResource):

    Tags = ToManyField('accounts_manager.api.resources.TagsResource', 'tags', null=True)
    Auditions = ToManyField('accounts_manager.api.resources.AuditionResource', 'auditions', null=True)

    class Meta:
        queryset = ActorProfile.objects.all()
        resource_name = "actor_profile"
        authorization = Authorization()


class TagResource(ModelResource):

    Actor = ToManyField('accounts_manager.api.resources.ActorResource', 'actors', null=True)
    Auditions = ToManyField('accounts_manager.api.resources.AuditionResource', 'auditions', null=True)

    class Meta:
        queryset = Tag.objects.all()
        resource_name = "tag"
        authorization = Authorization()

class ProductionResource(ModelResource):

    Tags = ToManyField('accounts_manager.api.resources.TagsResource', 'tags', null=True)
    Auditions = ToManyField('accounts_manager.api.resources.AuditionResource', 'auditions', null=True)

    class Meta:
        queryset = ProductionProfile.objects.all()
        resource_name = "production_profile"
        authorization = Authorization()



class AuditionResource(ModelResource):

    actors = ToManyField('accounts_manager.api.resources.ActorResource', 'actor_user', null=True)
    production = ToOneField('accounts_manager.api.resources.ProductionResource', 'production_user', full=True, null=True)
    parts = ToManyField('accounts_manager.api.resources.PartResource', 'parts', null=True, full=True)
    is_the_producer = fields.BooleanField()

    class Meta:
        queryset = Audition.objects.all()
        resource_name = "audition"
        authorization = Authorization()
        authentication = MultiAuthentication(BasicAuthentication(), Authentication())

    def dehydrate_is_the_producer(self, bundle):

        if bundle.request.user.is_anonymous() or not bundle.request.user.is_authenticated():
            return False
        try:
            producer = bundle.request.user.producer
        except ProductionProfile.DoesNotExist:
            return False
        return bundle.obj.production_user == bundle.request.user.producer


class PartResource(ModelResource):

    Audition = ToOneField('accounts_manager.api.resources.AuditionResource', 'audition')


    class Meta:
        queryset = Part.objects.all()
        resource_name = "part"
        authorization = Authorization()





######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)