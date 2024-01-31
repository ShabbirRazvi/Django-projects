from django.db import models

# Create your models here.


class Register_model(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Username = models.CharField(max_length=30)
    Password1 = models.CharField(max_length=20)
    Password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.First_name
