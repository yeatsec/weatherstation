from django.db import models

# Create your models here.

class WeatherData(models.Model):
	temperature = models.DecimalField(max_digits=5,decimal_places=2)
	pressure = models.DecimalField(max_digits=5,decimal_places=2)
	humidity = models.DecimalField(max_digits=5,decimal_places=2)
	light_intensity = models.DecimalField(max_digits=5,decimal_places=2)
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return 'Weather from: ' + str(self.created)
	
	class Meta:
		ordering = ('created',)

