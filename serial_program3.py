#!/bin/bash
import serial
import sqlite3
import time


conn = sqlite3.connect("temp_perfil.db")
cur = conn.cursor()
ser = serial.Serial("/dev/ttyACM0", 9600)

def is_number(s):
	try:
		float(s)
		return True
	except:
		return False


ser.readline()
ser.readline()
print "Start reading"
time.sleep(4)
for i in range(7):
	ser.readline()

while 1:
	print "Read: "
	info = ser.readline()
	print info
	info_arr = info.split("\t")
	info_arr = map(lambda x: x.strip(), info_arr)
	numbers = filter(lambda x: is_number(x), info_arr)
	try:
		print "Inserting"
		cur.execute("INSERT INTO sab3(temperature1, temperature2, humidity) VALUES(" + ", ".join(numbers) + ");")
		conn.commit()
	except:
		continue
	
