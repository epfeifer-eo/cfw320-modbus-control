# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:13:30 2025

@author: elija
"""
import minimalmodbus
import time

vfd = minimalmodbus.Instrument('COM5', 1)
vfd.serial.baudrate = 19200
vfd.serial.bytesize = 8
vfd.serial.parity = minimalmodbus.serial.PARITY_EVEN
vfd.serial.stopbits = 1
vfd.serial.timeout = 1
vfd.mode = minimalmodbus.MODE_RTU

vfd.write_register(221, 9, functioncode=6)  # Command source: serial (P682)
vfd.write_register(222, 9, functioncode=6)  # Speed ref: serial (P683)

vfd.write_register(683, 4096, functioncode=6)  # Set speed in Hz (X * 8192 / 60)
vfd.write_register(682, 0x0017, functioncode=6)  # Start command

time.sleep(10)  # Run 10 sec

vfd.write_register(682, 0, functioncode=6) # Stop motor: write 0 to P682
