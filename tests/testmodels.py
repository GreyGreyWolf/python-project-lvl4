from django.test import TestCase
from faker import Faker
from faker.generator import Generator
from tasks.models import Tag, Taskstatus, Task
from django.contrib.auth.models import User


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

    def test_object_name(self):
        taskstatus = Taskstatus.objects.get(id=1)
        expected_object_name = '%s' % taskstatus.name
        self.assertEquals(expected_object_name, str(taskstatus))


class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Testtag')

    def test_tag_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_tag_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_object_name(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = '%s' % tag.name
        self.assertEquals(expected_object_name, str(tag))


class TasksModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        tags = ''
        Taskstatus.objects.create(name='Teststatus')
        User.objects.create(username='Teststatus')
        Tag.objects.create(name='test')
        name_tag = Tag.objects.get(id=1)
        Task.objects.create(name='Testtask',
                            description='test',
                            status=Taskstatus.objects.get(id=1),
                            creator=User.objects.get(id=1),
                            assigned_to=User.objects.get(id=1),
                            tags.set(Tag.objects.name))

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
                                                           Taskstatus,
                                                           task.creator,
                                                           task.task.assigned_to,
                                                           task.tags)
        self.assertEquals(expected_object_name, str(task))
