# Here we will import all the extra functionality desired
from time import *
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)


def stop(x):
    kit.continuous_servo[x].throttle = 0


rear_motor = kit.continuous_servo[0]


def rotate_once(x):
    x = (x * 1.081) / 2
    print(x)
    rear_motor.throttle = 0.5
    sleep(x)
    stop(0)


rotate_once(1)
