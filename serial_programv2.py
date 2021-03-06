#!/bin/bash
import serial
import sqlite3
import time
from argparse import ArgumentParser


parser = ArgumentParser(description="Process data received from serial")
parser.add_argument('--mode', type=str, help="which logging mode")



args = parser.parse_args()


conn = sqlite3.connect("temp_perfil.db")
cur = conn.cursor()
ser = serial.Serial("/dev/ttyACM0", 9600)

def is_number(s):
	try:
		float(s)
		return True
	except:
		return False


if args.mode == "sab":

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
		info_arr = info.split(" ")
		numbers = filter(lambda x: is_number(x), info_arr)
		try:
			cur.execute("INSERT INTO medidas(humedad, temperaturaF) VALUES(" + ", ".join(numbers) + ");")
			conn.commit()
		except:
			continue
 	

elif args.mode == 'rumac':
	ser.readline()
	ser.readline()
	print "Start reading"
	time.sleep(4)
	for i in range(7):
		ser.readline()
	while 1:
		print "Read: "
		info = ser.readline()
		# here goes code on parsing shit
		numbers = info.split(" ")
		numbers = filter(lambda x: is_number(x), info_arr)
		try:
			cur.execute("INSERT INTO med_rumac(pressure, temperature) VALUE(" + ", ".join(numbers) +");")
			conn.commit()
		except:
			continue

	
