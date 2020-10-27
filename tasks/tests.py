from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.test import Client, TestCase
from faker import Faker
from faker.generator import Generator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SigninTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='test', password='12test12', email='test@example.com')

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
