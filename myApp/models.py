from django.db import models

class MyModel (models.Model):
	title = models.CharField(max_length = 255)
	contant = models.TextField()
	update = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.title