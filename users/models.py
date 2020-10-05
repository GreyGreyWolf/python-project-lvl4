from django.db import models


class User(models.Model):
    email = models.EmailField()
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    
    
    def __str__(self):
        return "%s %s %s" % (self.firstname, self.lastname, self.email)
    
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'