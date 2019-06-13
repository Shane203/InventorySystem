from django.db import models
from django.utils import timezone
import datetime

class Item(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.CharField(max_length=200)
	expiry_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	date_time_added = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
	
	def __str__(self):
		return self.name
	
	def due_to_expire(self):
	#Returns true if item is due to expire in 2 days or less or has already expired.
		return self.expiry_date - datetime.timedelta(days=2) <= timezone.now().date()


# Create your models here.
