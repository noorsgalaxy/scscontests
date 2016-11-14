__author__ = 'Galaxy'

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^profile', views.myprofile, name='myprofile'),
    url(r'^(?P<user>.{1,30})', views.visituser, name='visituser')
]