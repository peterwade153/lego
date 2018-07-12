from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Business, Reviews

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id','business_name', 'location', 'category', 'owner', 'created_on')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('review', 'business', 'reviewed_by', 'reviewed_on')

class UserSerializer(serializers.ModelSerializer):
    businesses = serializers.PrimaryKeyRelatedField(many=True, queryset=Business.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'businesses')