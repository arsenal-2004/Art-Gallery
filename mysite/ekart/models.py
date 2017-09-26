from django.db import models
import os

class Artist(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

def get_image_path(instance, filename):
	return os.path.join('paintings', str(instance.id), filename)

class Painting(models.Model):
	name = models.CharField(max_length=200)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def save(self, *args, **kwargs):
		if self.id == None:
			saved_image = self.image
			self.image = None
			super(Painting, self).save(*args, **kwargs)
			self.image = saved_image
			#kwargs.pop('force_insert')
		super(Painting, self).save(*args, **kwargs)

	def __str__(self):
		return self.name