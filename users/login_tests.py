from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user_model, get_user


class LoginTest(TestCase):
    def test_login(self):
        user = CustomUser.objects.create_user(username='baxtiyor01', first_name='Baxtiyor')
        user.set_password('qwerty1234')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'baxtiyor01',
                'password': 'qwerty1234'
            }
        )

        self.assertEqual(response.status_code,302)

        user_is_authenticated = response.wsgi_request.user.is_authenticated
        self.assertTrue(user_is_authenticated)

    def test_username_passsord(self):
        user = CustomUser.objects.create_user(username='baxtiyor01')
        user.set_password('qwerty1234')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'baxtiyor01',
                'password': 'qwerty1234'
            }
        )

        self.assertEqual(response.status_code, 302)

        user_is_authenticated = response.wsgi_request.user.is_authenticated
        self.assertTrue(user_is_authenticated)

