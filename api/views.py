from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Business, Reviews
from api.serializers import BusinessSerializer, ReviewSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly, IsNotOwner

class BusinessViewSet(viewsets.ModelViewSet):
    '''
    lists all registered businesses and also enables posting of new business
    '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        '''
        Will enable associate a user to business they registered
        '''
        serializer.save(owner=self.request.user )

class ReviewViewSet(viewsets.ModelViewSet):
    '''
    lists all reviews and also enables posting of new reviews
    '''
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, IsNotOwner)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

