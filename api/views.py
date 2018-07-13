from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from api.models import Business, Reviews
from api.serializers import BusinessSerializer, ReviewSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly

class BusinessList(generics.ListCreateAPIView):
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

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    fetches a single business, updates and also deletes
    '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

class ReviewList(generics.ListCreateAPIView):
    '''
    lists all reviews and also enables posting of new reviews
    '''
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

class UserList(generics.ListAPIView):
    '''
    list users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''
    list a particular user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

