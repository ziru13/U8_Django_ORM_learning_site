# 1. we're building a pretty good list of products but we need to start collecting reviews.
# 	 Can you create a 'Review' model for me?
# 	 To start with, give it a single field, 'rating', that is an 'InterField'

# 2. now we need to add a link between the 'Review' model and the 'Product' model,
# 	 add a new field to 'Review', named 'product', that is a 'ForeignKey' to 'Product' model

# 3. add a 'created_at' field that is DateTimeField with auto_now_add set to True,
# 	 then, add a comment field that is TextField,
# 	 it should have an empty string for its default



# products/models.py
from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	url = models.URLField()
	description = models.TextField(default='')
	price = models.DecimalField()

	def __str__(self):
		return self.name


class Review(models.Model):				# 1
	rating = models.IntegerField()		# 1
	product = models.ForeignKey(Product, on_delete=models.CASCADE)	 # 2
	create_at = models.DateTimeField(auto_now_add=True)				 # 3
	comment = models.TextField(default='')							 # 3

