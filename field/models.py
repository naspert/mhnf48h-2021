from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Observation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(max_length=200, help_text='Espèce')
    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(default=timezone.now)
    remarks = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.species
