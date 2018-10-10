import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AuthUserTest(APITestCase):
    '''
    test user login
    '''
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='fest123', password='fest1234567', email="ffest123@gmail.com")
        self.user.save()

    def test_register_with_valid_credentials(self):
        url='/api/v1/auth/login/'
        data = {'username':'fest123','password':'fest1234567'}
        response = self.client.post(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)