from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^businesses/$', views.BusinessList.as_view()),
    url(r'^businesses/(?P<pk>[0-9]+)/$', views.BusinessDetail.as_view()),
    url(r'^businesses/(?P<pk>[0-9]+)/reviews/$', views.ReviewList.as_view()),

    # urls to display users and their details
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    # authentication urls using django-rest-auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

]
