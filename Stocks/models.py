from django.db import models

# Create your models here.
class Stocks(models.Model):
	name = models.CharField(max_length=20,default="NULL")
	code = models.CharField(max_length=10,default="NULL")
	#open_price = models.DecimalField(max_digits=5, decimal_places=5)
	open_price = models.CharField(max_length=10,default="NULL")
	high_price = models.CharField(max_length=10,default="NULL")
	low_price  = models.CharField(max_length=10,default="NULL")
	
	def __str__(self):
		return self.name