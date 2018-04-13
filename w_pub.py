# weather publishing script
# Bind PUB socket to tcp://*:5556

from sense_hat import SenseHat
import zmq

# gather weather information
sense = SenseHat()
sense.set_rotation(180)

temp = sense.get_temperature()
press = sense.get_pressure()
hum = sense.get_humidity()

# publish weather information
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

socket.send_string("%s %s %s" % (temp, press, hum))