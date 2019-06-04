from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSignUpViewTest(TestCase):
    api_url = 'http://0.0.0.0:8000'

    def sign_up(self):
        url = '%s/register/' % self.api_url
        data = {
            'username': 'abv', 'password': 'qwerty123',
            'email': 'test@gmail.com', 'role': 1, 'balance': 100
        }

        r = self.client.post(url, data)

        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertTrue(r.data.get('token'))


class UserLoginViewTest(TestCase):
    api_url = 'http://0.0.0.0:8000/'

    def login(self):
        self.user = User.objects.create(
            username='adv',
            password='qwerty123',
        )
        self.user.set_password('qwerty123')
        self.user.save(update_fields=['password'])
        url = 'rest-auth/login/' % self.api_url
        data = {
            'username': 'abv',
            'password': 'qwerty123'
        }

        r = self.client.post(url, data)

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(r.data.get('token'))

