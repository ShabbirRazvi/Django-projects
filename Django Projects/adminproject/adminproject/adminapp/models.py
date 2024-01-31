from django.db import models

# Create your models here.


class Student(models.Model):
    sn = models.CharField(max_length=20)
    sr = models.IntegerField()
    sb = models.CharField(max_length=10)
    sc = models.BigIntegerField()

    def __str__(self):
        return self.sn
