from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

mh = Raspi_MotorHAT(addr=0x6f)
lm = mh.getMotor(1)
rm = mh.getMotor(2)

def turn_off_motors():
        lm.run(Raspi_MotorHAT.RELEASE)
        rm.run(Raspi_MotorHAT.RELEASE)
atexit.register(turn_off_motors)

lm.setSpeed(150) #Little over Half of 255 max speed
rm.setSpeed(150)

lm.run(Raspi_MotorHAT.FORWARD) #Placing OR  of these .BACKWARD will turn Robot 
rm.run(Raspi_MotorHAT.FORWARD) #Placing OR  of these .BACKWARD will turn Robot
time.sleep(1) #Disabled after 1 second
