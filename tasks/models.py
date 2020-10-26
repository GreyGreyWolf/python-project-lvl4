from django.db import models
from django.contrib.auth.models import User


class Taskstatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=128, blank=True)
    status = models.ForeignKey(Taskstatus, default=1, on_delete=models.CASCADE,
                               related_name='statuses')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="creators")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name="assigned_to")
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
