from rest_framework import serializers
from .models import WeatherData
	
class WeatherDataSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	temperature = serializers.DecimalField(max_digits=5,decimal_places=2)
	pressure = serializers.DecimalField(max_digits=5,decimal_places=2)
	humidity = serializers.DecimalField(max_digits=5,decimal_places=2)
	light_intensity = serializers.DecimalField(max_digits=5,decimal_places=2)

	def create(self,validated_data):
		return WeatherData.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.temperature = validated_data.get('temperature', instance.temperature)
		instance.pressure = validated_data.get('pressure', instance.pressure)
		instance.humidity= validated_data.get('humidity', instance.humidity)
		instance.light_intensity = validated_data.get('light_intensity', instance.light_intensity)
		instance.save()
