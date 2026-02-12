'''
Author(s): Darshan Ayyanar, Vihaan Cheepurupalli, Shrihan Vemula
Team Powersurge Storm 2025
This code solves 3 missions: Careful Recovery, Statue Rebuild & Mineshaft delivery
'''
import runloop
from hub import port
import motor_pair
from hub import motion_sensor
import motor
import color_sensor
import color

# Defining Port variables for easy access
LEFT = port.B # Left Drive wheel
RIGHT = port.D # Right Drive wheel
LEFT_ATTACHMENT = port.C 
RIGHT_ATTACHMENT = port.F

'''
Drive straight code using yaw angles to auto correct Robot's movement while driving forward
Inputs: 
  distance: Distance RObot has to Travel
  speed: velocity at which Robot has to travel
'''
async def gyro_forward(distance, speed):
    motor.reset_relative_position(LEFT, 0)
    motion_sensor.reset_yaw(0)
    steer = 0
    while(motor.relative_position(LEFT)>=(-1 * distance)):
        #print(motor.relative_position(LEFT))
        error = motion_sensor.tilt_angles()[0] * -0.1
        # correction is an integer which is the negative of the error
        correction = int(error * -2)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=speed)
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)

'''
Drive straight code using yaw angles to auto correct Robot's movement while driving back
Inputs:
distance: Distance Robot has to Travel
speed: velocity at which Robot has to travel
'''
async def gyro_backward(distance, speed):
    motion_sensor.reset_yaw(0)
    motor.reset_relative_position(LEFT, 0)
    steer = 0
    #print(motor.relative_position(LEFT))
    while(motor.relative_position(LEFT)<=distance):
        #print(motor.relative_position(LEFT))
        error = motion_sensor.tilt_angles()[0] * -0.1
        #print(error)
        # correction is an integer which is the negative of the error
        correction = int(error * 2)
        # print(correction)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity= (-1*speed))
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)

# main function to write code to move Robot and attachments
async def main():
    #Resetting Robot Yaw face and yaw angles before it makes any movements
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,LEFT,RIGHT) #creating new pair motors at        this whole chunk from 9 to 14 is to activate the driving motors and reseting the bot to move smoothly
    color_sensor.reflection(port.A)
    # *****Code for this run starts here *****

    # Before we start moving, lift both attachments up
    motor.run_for_degrees(LEFT_ATTACHMENT,300,600)
    motor.run_for_degrees(RIGHT_ATTACHMENT,500,600 )

    # Move forward all the way to hit the wall
    await gyro_forward(distance=1900,speed=800)

     #move back from wall to get turning room
    await gyro_backward(distance=100, speed=100)    
    
    # print(motion_sensor.tilt_angles()[0])

    #Make a right turn to align with Mineshaft using left wheel while reading tilt angles, 
    # and stop after it reaches desired yaw angle
    while(motion_sensor.tilt_angles()[0]>-850):
        motor.run(LEFT,-200)
    motor.stop(LEFT)

    # print(motion_sensor.tilt_angles()[0])

    # Move slightly back to get enough room to drop attachments down
    await gyro_backward(distance=75, speed=200)

    #Drop attachments 
    await motor.run_for_degrees(LEFT_ATTACHMENT, 300,-600)
    await motor.run_for_degrees(RIGHT_ATTACHMENT, 450,-600)

    #Move forward until Black color is detected
    while color_sensor.color(port.A) is not color.BLACK:
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=90)
        #if color_sensor.color(port.A) is color.BLACK:
        #    print("black")
    motor_pair.stop(motor_pair.PAIR_1)

    # Lift Right attachment to send Mineshaft to other side of the table
    await motor.run_for_degrees(RIGHT_ATTACHMENT, 450, 500)

    # Lift Left attachment to lift precious artifact with low velocity

    await motor.run_for_degrees(LEFT_ATTACHMENT, 60, 100)
    
    #Go back after grabbing artifact
    await gyro_backward(distance=220,speed=220)

runloop.run(main())
