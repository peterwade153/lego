from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^businesses/$', views.BusinessList.as_view()),
    url(r'^businesses/(?P<pk>[0-9]+)/$', views.BusinessDetail.as_view()),
    url(r'^businesses/(?P<pk>[0-9]+)/reviews/$', views.ReviewList.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]
