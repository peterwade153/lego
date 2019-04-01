from django.conf.urls import url, include,  re_path
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_auth.registration.views import VerifyEmailView, RegisterView

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
    url(r'^businesses/$', BusinessList.as_view(), name="businesses"),
    url(r'^businesses/(?P<pk>[0-9]+)/$', BusinessDetail.as_view(), name="business"),
    url(r'^businesses/(?P<id>[0-9]+)/reviews/$', ReviewList.as_view(), name="reviews"),
    # searching
    url(r'^businesses/search/$', SearchBusinessLists.as_view()),

    # authuentication urls
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/register/', include('rest_auth.registration.urls')),
    path('registration/', RegisterView.as_view(), name='account_signup'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
    name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
    name='account_confirm_email'),
]
