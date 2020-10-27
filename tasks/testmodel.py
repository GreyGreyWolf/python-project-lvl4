from django.test import TestCase
from faker import Faker
from faker.generator import Generator
from tasks.models import Tag, Taskstatus, Task


class TaskstatusModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Taskstatus.objects.create(name='Teststatus')

    def test_taskstatus_name_label(self):
        taskstatus = Taskstatus.objects.get(id=1)
        field_label = taskstatus._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_taskstatus_name_max_length(self):
        taskstatus = Taskstatus.objects.get(id=1)
        max_length = taskstatus._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Testtag')

    def test_tag_name_label(self):
        tag = Taskstatus.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_tag_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)


class TasksModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='Testtask')

    def test_task_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_taskstatus_name_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name(self):
        task = Task.objects.get(id=1)
        expected_object_name = '%s, %s, %s, %s, %s, %s' % (task.name,
                                                           task.description,
                                                           task.status,
                                                           task.creaotr,
                                                           task.task.assigned_to,
                                                           task.tags)
        self.assertEquals(expected_object_name, str(task))
