from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class event(models.Model):
     Image = models.ImageField(upload_to='Event_images/')
     EventName = models.CharField(max_length=50)
     Date = models.DateField()
     EventDescription = models.TextField(max_length = 400)
     likes = models.ManyToManyField(User,related_name='event_name',blank=True)