from django.db import models
from django.conf import settings


# Create your models here.
class Link(models.Model):
	id = models.AutoField(primary_key=True)
	long = models.TextField()
	publsh = models.DateTimeField(auto_now=True)

	def short(self) -> str:
		out = ''
		dec = self.pk
		while dec > 1:
			out += settings.BASE_SYMBOLS[dec % settings.BASE]
			dec //= settings.BASE
		return out

