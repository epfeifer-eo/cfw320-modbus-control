# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:01:06 2025

@author: elija
"""
import minimalmodbus
import time

instrument = minimalmodbus.Instrument('COM5', 1)  # (port name, slave address)
instrument.serial.baudrate = 19200
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout = 1  # seconds
instrument.mode = minimalmodbus.MODE_RTU

# DO1 ON (bit 0 of P695 = 1)
instrument.write_register(0x02B7, 0x0001, functioncode=6)  # P695 = 1
time.sleep(1)
# DO1 OFF
instrument.write_register(0x02B7, 0x0000, functioncode=6)  # P695 = 0
time.sleep(1)
instrument.write_register(0x02B7, 0x0001, functioncode=6)  # P695 = 1
time.sleep(1)
instrument.write_register(0x02B7, 0x0000, functioncode=6)  # P695 = 0
time.sleep(1)
instrument.write_register(0x02B7, 0x0001, functioncode=6)  # P695 = 1
time.sleep(1)
instrument.write_register(0x02B7, 0x0000, functioncode=6)  # P695 = 0