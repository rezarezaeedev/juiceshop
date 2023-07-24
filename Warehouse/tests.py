from rest_framework.test import APITestCase
from rest_framework import status
from .models import Juice, Brand
import random
import string
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


User = get_user_model()

def get_random_string(length=10):
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


class JuiceTests(APITestCase):
	fields = ['flavour', 'ice', 'nic', 'capacity', 'salt', 'brand', 'price']

	def setUp(self):
		self.user = User.objects.create(username='testuser', is_staff=1, is_superuser=1)
		self.brand = Brand.objects.create(name=get_random_string(), country=get_random_string())

	def test_create_juice_model(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.user).access_token}'
		data = {
			'flavour':get_random_string(),
			'brand':self.brand.pk,
			'salt':random.choice([True, False]),
			'ice':random.choice([True, False]),
			'nic':random.randint(1, 50),
			'capacity':random.randint(1, 500),
			'price':random.randint(100,100000),
		}
		self.client.credentials(HTTP_AUTHORIZATION=authorizer)
		response = self.client.post(url, data)
		print(response.status_code)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)

