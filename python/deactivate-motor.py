# paste into python shell to use stop() command, place motor slot in parenthesess

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
# defining function to stop motors
def stop(x):
    kit.continuous_servo[x].throttle = 0


stop(2)
