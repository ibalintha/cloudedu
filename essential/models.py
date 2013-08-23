import datetime
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class DataDict(models.Model):
	code = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	status = models.BooleanField()
	order = models.IntegerField()
	create_date = models.DateTimeField(null=True, default=datetime.datetime.now())

	def get_absolute_url(self):
		return reverse('datadict-update', kwargs={'pk': self.pk})
