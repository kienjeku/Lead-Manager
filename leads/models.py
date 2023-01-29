from django.db import models
from django.utils import timezone

class Lead(models.Model):

    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    message = models.CharField(max_length = 300)
    date_created = models.DateTimeField(default = timezone.now)

