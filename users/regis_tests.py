from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user_model
import re


# Create your tests here.

class UserRegistrationTest(TestCase):
    def test_create_user(self):
        self.client.post(
            reverse('users:regis'),
            data={
                'username': 'admin1',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'email': 'email@gmail.com',
                'password': 'baxtiyor123'
            }
        )

        user = get_user_model().objects.get(username='admin1')
        self.assertEqual(user.first_name, 'Admin')
        self.assertEqual(user.email, 'email@gmail.com')
        self.assertTrue(user.check_password, 'baxtiyor123')

    def test_required_fields(self):
        res = self.client.post(
            reverse('users:regis'),
            data={
                'first_name': 'Admin',
                'last_name': 'Adminov',
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertTrue(res, 'This field is required.')

    def test_double_user(self):
        user = CustomUser.objects.create_user(username='baxtiyor01', first_name='Baxtiyor')
        user.set_password('qwerty1234')
        user.save()

        res = self.client.post(
            reverse('users:regis'),
            data={
                'username': 'baxtiyor01',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'email': 'email@gmail.com',
                'password': 'baxtiyor123'
            }
        )

        username_count = CustomUser.objects.count()
        self.assertEqual(username_count, 1)
        self.assertContains(res)

    def test_email_1(self):
        res = self.client.post(
            reverse('users:regis'),
            data={
                'username': 'admin1',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'email': 'email@gmail.com',
                'password': 'baxtiyor123'
            }
        )

        email_count = CustomUser.objects.count()
        self.assertEqual(email_count, 1)  # yuqoridagi emailni sanash uchun bu qator ishlatiladi
        self.assertTrue(res, 'Enter a valid email address')


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


class EmailTestCase(TestCase):
    def test_email_2(self):
        # To'g'ri email formatini tekshirish
        email = 'email@gmail.com'
        self.assertTrue(is_valid_email(email))

        # Noto'g'ri email formatini tekshirish
        email = 'invalid_email'
        self.assertFalse(is_valid_email(email))
