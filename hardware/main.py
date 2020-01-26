from __future__ import division
from __future__ import absolute_import
import serial
import time
import urllib2
import random
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
ser.flush()
def velocity(h):
	return pow((h)/(.5 * 9.8), .5)*9.8
def flow(h, d):
	return pow(d/2, 2) * 3.14159 * velocity(h)

height = 7 * 0.0254
diameter = 2 * 0.0254
username = 'mitchell'
password = 'testpassmitchell'
while (True):
	r = ser.readline()
	if r.strip() == '1':
		#print 'wet'
		start = time.time()
		while(True):
			if ser.readline().decode().strip('\r\n') == '0':
				break
		end = time.time()
		#print(end - start)
		second = (end - start)
		#print r
		#volume = (flow(height, diameter) * 1000 * second)
		volume = random.uniform(23,25) * 0.0078125
		print volume
		urllib2.urlopen('http://localhost:5000/addevent/' + username + '/' + password + '/faucet/' + str(int(start)) + '/' + str(int(end)) + '/'+ str(volume) + '/')

