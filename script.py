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


# This function will allow us to move the car in any way

# a = Speed of car
# b = Specifies fowards or backwards movement
# c = How much the car will turn

def move(a, b, c,):
    # This is a filler so we don't get any errors when testing other code
    print("There will be code here")
