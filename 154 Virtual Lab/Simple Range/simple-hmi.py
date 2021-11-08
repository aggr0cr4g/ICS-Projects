#!/usr/bin/env python

"""
SYNOPSIS
    TODO helloworld [-h] [-v,--verbose] [--version]
DESCRIPTION
    TODO This describes how to use this script.
    This docstring will be printed by the script if there is an error or
    if the user requests help (-h or --help).
  MODBUS 984 Address for   
    X001 = 100001
    X002 = 100002
	Y002 = 8193 = Green Light
	Y003 = 8194 = Red Light
"""
from pymodbus.client.sync import ModbusTcpClient
import time

def main ():
	client = ModbusTcpClient('192.168.1.130')
	while True:
		val = input("[r] for read [w] for write [s] stop: ")
		if val == 'r':
			red = client.read_coils(8194,1)
			green = client.read_coils(8193,1)
			print('Red Light status is',red.bits[0])
			print('Green Light status is',green.bits[0])
			client.close()
		if val == 'w':
			val1 = input("[g] for green [w] for red: ")
			val2 = int(input("[1] for True or [0] for False: "))
			if val1 == 'g':
				client.write_coil(8193, val2)
			if val1 == 'r':
				client.write_coil(8194, val2)
			client.close()
		if val == 's':
			break


if __name__ == '__main__':
	main ()