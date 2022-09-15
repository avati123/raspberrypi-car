# Here we will import all the extra functionality desired
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#Pin 8 = Left Motor
#Pin 12 = Right Motor


def stop(x):
    kit.continuous_servo[x].throttle = 0


def stopall():
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[1].throttle = 0
    kit.continuous_servo[2].throttle = 0
    kit.continuous_servo[3].throttle = 0
    kit.continuous_servo[4].throttle = 0
    kit.continuous_servo[5].throttle = 0
    kit.continuous_servo[6].throttle = 0
    kit.continuous_servo[7].throttle = 0
    kit.continuous_servo[8].throttle = 0
    kit.continuous_servo[9].throttle = 0
    kit.continuous_servo[10].throttle = 0
    kit.continuous_servo[11].throttle = 0
    kit.continuous_servo[12].throttle = 0
    kit.continuous_servo[13].throttle = 0
    kit.continuous_servo[14].throttle = 0
    kit.continuous_servo[15].throttle = 0
    kit.continuous_servo[16].throttle = 0


left_rear_motor = kit.continuous_servo[8]
right_rear_motor = kit.continuous_servo[12]
rear_motors = left_rear_motor + right_rear_motor


def rotate_once(x):
    x = (x * 1.081) / 2
    print(x)
    rear_motors.throttle = 0.5
    sleep(x)
    stop(0)


rotate_once(1)

# This function will allow us to move the car in any way

# a = Speed of car
# b = Specifies fowards or backwards movement
# c = How much the car will turn


def move(a, b, c):
    print("there is code here")
