from django.db import models

# Create your models here.
class Link(models.Model):
	id = models.AutoField(primary_key=True)
	short = models.CharField(max_length=50)
	long = models.TextField()
	publsh = models.DateTimeField(auto_now=True)
