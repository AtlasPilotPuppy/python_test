from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
    url(r'^todo/', todo, name='todo'),
    url(r'^save_todo/', save_todo, name='save_todo'),
    url(r'^update_todo/', update_todo, name='update_todo'),
    url(r'^remove_todo/', remove_todo, name='remove_todo'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
)
