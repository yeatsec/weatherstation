import requests
import random

class URLPost():
	url = 'https://afternoon-garden-70836.herokuapp.com/updateWeather'
	def __init__(self, temp=80, humidity=20,press=30,location='Nashville'):
		self.temperature = temp
		self.humidity = humidity
		self.pressure = press
		self.location = location
		self.data = {'temperature' : self.temperature,
				'humidity'	  : self.humidity,
				'pressure'	: self.pressure,
				'location' : self.location
		}
		self.r = None
	
	def getRandomTemp(self):
		return random.randint(-10,110)

	def getRandomHumidity(self):
		return random.randint(0,101)
	
	def getRandomPressure(self):
		return random.randint(20,100)

	def getLocation(self):
		r = requests.get('https://api.ipdata.co')
		r = r.json()
		return {'city':r['city'],
				'country':r['country_name']	}

	def randomizeData(self):
		self.data = {'temperature' : self.getRandomTemp(),
				'humidity'	  : self.getRandomHumidity(),
				'location' : self.getLocation(),
				'pressure' : self.getRandomPressure()
		}
	
	def send(self):
		self.r = requests.post( url=self.url,
							data=self.data)
	
	def postStatusOk(self):
		if self.r is not None:
			return self.r.status_code == 200
		return False
