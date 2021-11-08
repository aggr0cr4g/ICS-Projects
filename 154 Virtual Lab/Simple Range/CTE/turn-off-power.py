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
	client.write_coil(8194, 0)
	client.write_coil(8193, 1)


if __name__ == '__main__':
	main ()