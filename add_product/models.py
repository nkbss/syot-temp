from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	img = models.ImageField(upload_to='static/add_product/images/')
	create_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title