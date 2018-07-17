from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views.auth_views import UserViewSet
from api.views.business_views import BusinessList, BusinessDetail, SearchBusinessLists
from api.views.review_views import ReviewList

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'businesses', BusinessViewSet)
# router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),

    # reviewing business
    url(r'^businesses/$', BusinessList.as_view()),
    url(r'^businesses/(?P<pk>[0-9]+)/$', BusinessDetail.as_view()),
    url(r'^businesses/(?P<id>[0-9]+)/reviews/$', ReviewList.as_view()),
    # searching
    url(r'^businesses/search/$', SearchBusinessLists.as_view()),

    # authuentication urls
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/register/', include('rest_auth.registration.urls')),
]
