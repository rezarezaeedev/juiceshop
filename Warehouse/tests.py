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
	fields = ['flavour', 'ice', 'nic', 'capacity', 'brand', 'price']

	def setUp(self):
		self.superuser = User.objects.create(username='testuser', is_staff=1, is_superuser=1)
		self.brand = Brand.objects.create(name=get_random_string(), country=get_random_string())

	def test_create_juice_model(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.superuser).access_token}'
		data = {
			'flavour':get_random_string(),
			'brand':self.brand.pk,
			'ice':random.choice([True, False]),
			'nic':random.randint(1, 50),
			'capacity':random.randint(1, 500),
			'price':random.randint(100,100000),
		}
		self.client.credentials(HTTP_AUTHORIZATION=authorizer)
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
		for field in self.fields:
			self.assertEqual(data[field], response.data[field], msg=f'Two {field=} values are not equals. ')


	def test_get_salt_serializer_method(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.superuser).access_token}'
		salt_flag = False
		nic = 3
		for i in range(2):
			data = {
				'flavour':get_random_string(),
				'brand':self.brand.pk,
				'ice':random.choice([True, False]),
				'nic':nic,
				'capacity':random.randint(1, 500),
				'price':random.randint(100,100000),
			}
			self.client.credentials(HTTP_AUTHORIZATION=authorizer)
			response = self.client.post(url, data)
			self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
			self.assertEqual(response.data['nic'], nic)
			self.assertEqual(response.data['salt'], salt_flag)
			nic = 50
			salt_flag = True


class BrandTests(APITestCase):

	def setUp(self):
		self.superuser = User.objects.create(username='testuser', is_staff=1, is_superuser=1)

	def test_create_brand_model(self):
		url = reverse('warehouse:brand-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.superuser).access_token}'
		data = {
			'country':get_random_string(),
			'name':get_random_string(),
		}
		self.client.credentials(HTTP_AUTHORIZATION=authorizer)
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
		self.assertEqual(response.data['name'], data['name'])
		self.assertEqual(response.data['country'], data['country'])


class PermissionTests(APITestCase):
	def setUp(self):
		self.length = 5
		self.superuser = User.objects.create(username='test superuser', is_staff=1, is_superuser=1)
		self.staffuser = User.objects.create(username='test staffuser', is_staff=1, is_superuser=0)
		self.normal = User.objects.create(username='test normaluser', is_staff=0, is_superuser=0)
		self.brand = Brand.objects.create(name=get_random_string(), country=get_random_string())
		for _ in range(self.length):
			Juice.objects.create(flavour=get_random_string(), brand=self.brand, nic=1, salt=0, ice=1, capacity=10, price=10, )


	def test_get_list_juice_objects_without_authentication(self):
		url = reverse('warehouse:juice-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
		data = response.data['results']
		self.assertEqual(response.data['count'], self.length, msg=f'given data length not equals with count if created objects.')
		self.assertEqual(data[0]['id'], Juice.objects.get(flavour=data[0]['flavour']).id)


	def test_create_success_juice_object_by_superuser(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.superuser).access_token}'
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
		self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)


	def test_create_fail_juice_object_by_staffuser(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.staffuser).access_token}'
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
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)


	def test_auth_fail_post_creating_juice_object(self):
		url = reverse('warehouse:juice-list')
		authorizer = f'Bearer {RefreshToken.for_user(self.superuser).access_token}'
		data = {
			'flavour':get_random_string(),
			'brand':self.brand.pk,
			'salt':random.choice([True, False]),
			'ice':random.choice([True, False]),
			'nic':random.randint(1, 50),
			'capacity':random.randint(1, 500),
			'price':random.randint(100,100000),
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)



