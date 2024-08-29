from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lecture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user}, Age: {self.age}"

class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    # rate = models.FloatField(default=0)
    # count = models.IntegerField(default=0)
    creator = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

