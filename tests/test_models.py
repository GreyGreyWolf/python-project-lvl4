from django.test import TestCase
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


class TaskModelTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='test1', password='1q2w3e4r', email='test@example.com')
        self.user2 = User.objects.create_user(
            username='test2', password='1q2w3e4r', email='test@example.com')
        self.user1.save()
        self.user2.save()
        self.status = Taskstatus.objects.create(name='test')
        self.status.save()
        self.task = Task(name='TestTask',
                         description='description',
                         status=self.status,
                         creator=self.user1,
                         assigned_to=self.user2)
        self.task.save()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_name_max_length(self):
        max_length = self.task._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_task_name(self):
        self.assertEquals(self.task.name, str(self.task))

    def test_read_task(self):
        self.assertEqual(self.task.status, self.status)
        self.assertEqual(self.task.creator, self.user1)
        self.assertEqual(self.task.assigned_to, self.user2)
        self.assertEqual(self.task.description, 'description')

    def test_update_task_(self):
        self.task.description = 'new description'
        self.task.assigned_to = self.user1
        self.task.save()
        self.assertEqual(self.task.description, 'new description')
        self.assertEqual(self.task.assigned_to, self.user1)
