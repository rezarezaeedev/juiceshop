from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

class RegisterationTests(APITestCase):
	def test_register_view(self):
		url = reverse('accounts:register')
		data = {
			'username': 'testusername',
			'password':'abcdefg',
			'password2':'abcdefg',
		}

		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['username'], data['username'])
		self.assertIsNotNone(response.data.get('token'), msg='Token not found!')