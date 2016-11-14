from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contests_list, name='contests_list'),
    url(r'^register/(?P<cid>\d{0,3})$',views.register, name='register'),
    url(r'^v/(?P<cid>)\d{0,3}$',views.contests_view, name='contests_view')
]