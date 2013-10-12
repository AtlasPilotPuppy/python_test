from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('todo.views',
    url(r'^$','tasklist', name='tasklist'),
    url(r'^create/$', 'create_task', name='create'),
    url(r'^delete/$', 'delete_task' , name='delete'),
    url(r'^toggle/$', 'toggle_task', name='toggle'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
)

#urlpatterns += patterns('',
#    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#)
