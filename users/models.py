from django.db import models
from groups.models import Group

# Create your models here.

class User(models.Model):
    user = models.CharField(
        max_length=20,
        blank=False,
        verbose_name= 'enter you nickname'
    )

    create = models.DateTimeField(
        auto_now= False
    )
    groups = models.ManyToManyField(
        to = Group
    )