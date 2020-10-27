from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.test import Client, TestCase
from auth.models import SiteUser
from faker import Faker
from faker.generator import Generator


class SuccessRegistrationTest(TestCase):

    def setUp(self):
        self.client: Client = Client()
        self.faker: Generator = Faker()

    def test(self):
        email: str = self.faker.email()
        fake_password: str = self.faker.password(length=10)
        user_name: str = self.faker.user_name()
        response: TemplateResponse = self.client.post(
            reverse_lazy('auth:registration'),
            data={
                'email': email,
                'username': user_name,
                'password1': fake_password,
                'password2': fake_password,
            },
        )
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(
            SiteUser.objects.filter(email=email, username=user_name),
        )



