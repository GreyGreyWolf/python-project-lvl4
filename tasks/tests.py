from django.test import TestCase
from faker import Faker
from faker.generator import Generator
from tasks.models import Tag, Taskstatus


class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.object.create(name='Test')

    def test_tag_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_tag_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
