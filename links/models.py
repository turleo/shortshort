from django.db import models
from datetime import datetime

# Create your models here.
class Link(models.Model):
	short = models.CharField(max_length=50, default=datetime.now())
	long = models.TextField()
	publsh = models.DateTimeField(auto_now=True)
