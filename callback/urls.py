from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from tastypie.api import Api
from accounts_manager.api.resources import ActorResource, TagResource, ProductionResource, AuditionResource

admin.autodiscover()


v1_api = Api(api_name="v1")
v1_api.register(ActorResource())
v1_api.register(TagResource())
v1_api.register(ProductionResource())
v1_api.register(AuditionResource())







urlpatterns = patterns('',



    url(r'^admin/', include(admin.site.urls)),



    url('index/', 'accounts_manager.views.index', name='index'),
    url('signup/', 'accounts_manager.views.signup', name='signup'),
    url('login_page/', 'accounts_manager.views.login_page', name='login_page'),
    url('profile_builder/', 'accounts_manager.views.profile_builder', name='profile_builder'),
    url('production_profile_builder/', 'accounts_manager.views.production_profile_builder', name='production_profile_builder'),


    url(r'^accounts/password/change/$',
        auth_views.password_change,
        name='password_change'),
    url(r'^accounts/password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
    url(r'^accounts/password/reset/$',
        auth_views.password_reset,
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),

    url(r'^api/', include(v1_api.urls)),

    url(r'accounts/', include('registration.backends.default.urls')),
)
