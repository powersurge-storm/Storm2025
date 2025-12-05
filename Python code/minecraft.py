# Author(s): Shrihan Vemula & Amelia Easter
# Team Powersurge Storm 2025
# This code solves 1 mission and sends Minecraft to other Team's board, and scores 30-40 points

from hub import light_matrix
import runloop
from hub import port
import motor_pair
from hub import motion_sensor
import motor
async def main():
    # write your code here
    #await light_matrix.write("Hi!")
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.pair(motor_pair.PAIR_1, port.B,port.D)# Define Motors

    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D) #creating new pair motors at        this whole chunk from 9 to 14 is to activate the driving motors and reseting the bot to move smoothly

    motor_pair.move(motor_pair.PAIR_1,0,velocity=500) #move forward
    await runloop.sleep_ms(2800) #waits for 2 seconds Move forward and stop but not immediately, move for 2 seconds and then stop
    motor_pair.stop(motor_pair.PAIR_1)#makes it stop 16-18 is making it move forward.motor_pair.move means two motors moving at the same time 16-17 is to move certain motor pair a certain way
    
    
    #Turn Right
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]>-900:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100)#move to Right
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

    motor_pair.move(motor_pair.PAIR_1,0,velocity=500) #move forward
    await runloop.sleep_ms(1300) #waits for 2 seconds Move forward and stop but not immediately, move for 2 seconds and then stop
    motor_pair.stop(motor_pair.PAIR_1)#makes it stop 16-18 is making it move forward.motor_pair.move means two motors moving at the same

    await motor.run_for_degrees(port.D, 500, 500)

    motor.run(port.F, 90,acceleration=1500)
    await runloop.sleep_ms(4800)
    motor.stop(port.F)

    motor_pair.move(motor_pair.PAIR_1,0,velocity=500) #move forward
    await runloop.sleep_ms(350) #waits for 2 seconds Move forward and stop but not immediately, move for 2 seconds and then stop
    motor_pair.stop(motor_pair.PAIR_1)#makes it stop


    # After solving
    # Move back    
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -300, 0)

    # Turn Right
    await motor.run_for_degrees(port.D, 500, -500)

     # Move back
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -500, 0)

    # Turn Left
    await motor.run_for_degrees(port.D, 500, 500)

     # Move back to Base
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -1800, 0,velocity=1000)


runloop.run(main())
