from django.test import TestCase
from faker import Faker
from faker.generator import Generator
from tasks.models import Tag, Taskstatus


class TaskstatusModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Taskstatus.objects.create(name='Teststatus')

    def test_tag_name_label(self):
        taskstatus = Taskstatus.objects.get(id=1)
        field_label = taskstatus._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_tag_name_max_length(self):
        taskstatus = Taskstatus.objects.get(id=1)
        max_length = taskstatus._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
