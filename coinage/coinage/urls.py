from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coinage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "core.views.index"),
    (r'^facebook/', include('django_facebook.urls')),
	(r'^accounts/', include('django_facebook.auth_urls')),
)
