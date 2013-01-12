from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pollerApp.views.home', name='home'),
    url(r'^login/$', 'pollerApp.views.login', name='login'),
    url(r'^logout/$', 'pollerApp.views.logout', name='logout'),
    url(r'^register/$', 'pollerApp.views.register', name='register')
    )
