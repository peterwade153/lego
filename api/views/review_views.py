from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status

from api.models import Business, Reviews
from api.serializers import ReviewSerializer
from api.permissions import IsOwnerOrReadOnly, IsNotOwner

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
        return Reviews.objects.filter(business_id=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        '''
        creating new reviews
        '''
        try:
            business = Business.objects.get(id=self.kwargs['id'])
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

