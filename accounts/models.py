from django.db import models
class User(models.Model):
    username=models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.username
