from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import Business

class BusinessTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='fest123', password='fest1234567', email="ffest123@gmail.com")
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.business_data = {'business_name':"weconnect", 'location':"kampala", 'category':'transport', 'owner':user.id}
        self.response = self.client.post(reverse('businesses'), self.business_data, format="json")

    def test_api_can_create_a_business(self):
        """Test the api has business creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


