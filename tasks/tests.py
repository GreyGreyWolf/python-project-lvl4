from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from tasks import views
from tasks.models import Tag, Task, Taskstatus


class TaskTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='1q2w3e4r5T',
        )
        self.client = Client()

    def createTask(self, name="test_name"):
        test_status = Taskstatus.objects.create(name='test')
        test_tag = Tag.objects.create(name='Test')
        test_task = Task.objects.create(
            name=name,
            description='Description for test',
            assigned_to=self.user,
            creator=self.user,
            status=test_status,
        )
        test_task.tags.set([test_tag])
        return test_task

    def test_task_create(self):
        test_task = self.createTask()
        self.assertTrue(isinstance(test_task, Task))
        self.assertEqual(test_task.__str__(), test_task.name)
        self.assertEqual(Task.objects.count(), 1)
