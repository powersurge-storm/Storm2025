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


async def main():
  # write your code here
    #Setting initial Yaw angle on motion_sensor
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
   
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D) #creating new pair motors at

    # Move driving motors for 1300 degrees
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1300, 0, velocity=600, acceleration= 100, deceleration=100)

    #Use Attatchment
    await motor.run_for_degrees(port.C, 200,200)

    #Turn Right
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]>-900:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100)#move to Right
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

    # Until White color is detected, move Robot back slowly
    while not color_sensor.color(port.A) is not color.WHITE:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, -50, 0)

    # Turn for 150 degrees after color sensor detects white
    await motor.run_for_degrees(port.D,150,150)

    #Turn Left
    while motion_sensor.tilt_angles()[0]<900:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,-100)#move to left
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

     # Move for 2 seconds
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2000, -10, velocity=-500) 
    
runloop.run(main())
