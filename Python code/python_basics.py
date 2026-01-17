# Python basics code
# Author: PowerSurge Storm students of 2025
# This project includes basic code snippets used within Spike Prime for solving FLL missions.

import runloop
import hub
from hub import port
import motor_pair
from hub import motion_sensor
import motor
import color_sensor
import color

LEFT = port.B
RIGHT = port.D
LEFT_ATTACHMENT = port.C
RIGHT_ATTACHMENT = port.F

async def gyro_forward(distance, speed):
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor.reset_relative_position(LEFT, 0)
    steer = 0
    while(motor.relative_position(LEFT)>=(-1 * distance)):
        error = motion_sensor.tilt_angles()[0] * -0.1
        correction = int(error * -2)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=speed)
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)

async def gyro_backward(distance, speed):
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor.reset_relative_position(LEFT, 0)
    steer = 0
    print(motor.relative_position(LEFT))
    while(motor.relative_position(LEFT)<=distance):
        error = motion_sensor.tilt_angles()[0] * -0.1
        # correction is an integer which is the negative of the error
        correction = int(error * 2)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity= (-1*speed))
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,LEFT,RIGHT) #creating new pair motors to activate the driving motors and reseting the bot to move smoothly
    
    # Move forward to be close to the Map reveal
    await gyro_forward(distance=1430,speed=500)

     # Until White color is detected, move Robot back slowly
    while not color_sensor.color(port.A) is not color.WHITE:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, -50, 0)

    #Turn Right
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]>-900:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100)#move to Right
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

    # Move driving motors for 1300 degrees
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1300, 0, velocity=600, acceleration= 100, deceleration=100)

    # Turn for 150 degrees after color sensor detects white
    await motor.run_for_degrees(port.D,150,150)

    
    #Use Attatchment
    await motor.run_for_degrees(port.C, 200,200)

    #Turn Left
    while motion_sensor.tilt_angles()[0]<900:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,-100)#move to left
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

     # Move for 2 seconds
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2000, -10, velocity=-500) 
    
runloop.run(main())
