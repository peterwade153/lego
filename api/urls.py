from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'businesses', views.BusinessViewSet)
# router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),

    # reviewing business
    url(r'^businesses/(?P<id>[0-9]+)/reviews/$', views.ReviewList.as_view()),

    # authuentication urls
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/register/', include('rest_auth.registration.urls')),
]

