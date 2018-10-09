from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=12)
    user_sex = models.BooleanField(default=True)
    user_age = models.IntegerField(default=20)
    user_icon = models.ImageField()