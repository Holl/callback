from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url('index/', 'accounts_manager.views.index', name='index'),
    url('signup/', 'accounts_manager.views.signup', name='signup'),
    url('login_page/', 'accounts_manager.views.login_page', name='login_page'),
    url('profile_builder/', 'accounts_manager.views.profile_builder', name='profile_builder'),


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

    url(r'accounts/', include('registration.backends.default.urls')),
)
