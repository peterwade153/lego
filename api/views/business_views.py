from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from api.models import Business
from api.serializers import BusinessSerializer
from api.permissions import IsOwnerOrReadOnly

class BusinessList(generics.ListCreateAPIView):
    '''
    Adding a new business
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
    Retrieve, Edit and Delete a Business
    '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )


class SearchBusinessLists(generics.ListAPIView):
    '''
    search by business name, location and category
    '''
    serializer_class = BusinessSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        location = self.request.query_params.get('location', None)
        category = self.request.query_params.get('category', None)
        queryset = Business.objects.all()
        if q is not None:
            return queryset.filter(business_name__search=q)
        if location is not None:
            return queryset.filter(location__search=location)
        if category is not None:
            return queryset.filter(category__search=category)
        return queryset

        