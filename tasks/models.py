from django.db import models
from users.models import User


class Taskstatus(models.Model):
    LIST_STATUSES = [
        ('NEW', 'New'),
        ('IN_WORK', 'In work'),
        ('ON_TESTING', 'On testing'),
        ('COMPLETED', 'Completed'),
    ]
    name = models.CharField(max_length=15, blank=False, null=False, choices=LIST_STATUSES, default='NEW')
    
    def __str__(self):
        return "Status %s" % self.name
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Task status"
    
    
class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    def __str__(self):
        return "Tag %s" % self.name
    
    
class Task(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=128, blank=True, null=True, default=None)
    status = models.ForeignKey(Taskstatus,default=1, on_delete=models.CASCADE,
                              related_name="status")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, 
                                    related_name ="creator")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, 
                                    related_name ="assigned_to")
    tags = models.ManyToManyField(Tag,related_name="tags", blank=True)
    
    def __str__(self):
        return "%s %s %s %s" % (self.name, self.status, self.assigned_to, self.creator)
    
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        
