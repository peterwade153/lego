from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status

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


class ReviewList(generics.ListCreateAPIView):
    '''
    Creating and viewing reviews
    '''
    model = Reviews
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        '''
        List all business reviews
        '''
        id = self.kwargs['id']
        return Reviews.objects.filter(business_id=id)


    def post(self, request, *args, **kwargs):
        '''
        creating new reviews
        '''
        id = self.kwargs['id']
        try:
            business = Business.objects.get(id=id)
            data = {
                'review':request.data['review'],
                'business':business.id,
                'reviewed_by':request.user.id
            }
            serializer = ReviewSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Business.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

