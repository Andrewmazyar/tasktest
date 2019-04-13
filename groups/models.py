from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(
        max_length= 55,
        blank= False,
        verbose_name='enter_groups_name'
    )

    description = models.TextField(
        blank=False,
        verbose_name="enter_description_of_group"
    )