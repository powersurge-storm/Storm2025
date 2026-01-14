# import runloop                                                             
from hub import port                                                              
import motor_pair
from hub import motion_sensor
import motor
import runloop


LEFT = port.B
RIGHT = port.D
LEFT_ATTACHMENT = port.C
RIGHT_ATTACHMENT = port.F

async def gyro_forward(distance, speed):
    motor.reset_relative_position(LEFT, 0)
    steer = 0
    while(motor.relative_position(LEFT)>=(-1 * distance)):
        #print(motor.relative_position(LEFT))
        error = motion_sensor.tilt_angles()[0] * -0.1
        # correction is an integer which is the negative of the error
        correction = int(error * -2)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity=speed)
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)

async def gyro_backward(distance, speed):
    motor.reset_relative_position(LEFT, 0)
    steer = 0
    print(motor.relative_position(LEFT))
    while(motor.relative_position(LEFT)<=distance):
        #print(motor.relative_position(LEFT))
        error = motion_sensor.tilt_angles()[0] * -0.1
        #print(error)
        # correction is an integer which is the negative of the error
        correction = int(error * 2)
        # print(correction)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity= (-1*speed))
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)
    print('done')

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,LEFT,RIGHT) #creating new pair motors at        this whole chunk from 9 to 14 is to activate the driving motors and reseting the bot to move smoothly
    
    # *****Code for this run starts here *****

    # Move forward to be close to the Map reveal
    await gyro_forward(distance=1430,speed=500)
    
    #Make a right turn to align with Mineshaft using left wheel
    await motor.run_for_degrees(LEFT, 480, -400)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1,400,0)

    #Left attachment down to ground
    await motor.run_for_degrees(LEFT_ATTACHMENT, 250, 500)

    #Make a right turn towards seal using right wheel
    await motor.run_for_degrees(RIGHT, 320, -400)

    # Lft attachment down 
    await motor.run_for_degrees(LEFT_ATTACHMENT, 350, -500)

    #Move fwd to align attachment be under seal
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,480,0)

    #Left attachment up to lift seal
    await motor.run_for_degrees(LEFT_ATTACHMENT, 180, 600)

    #Make a slight left turn to fix seal with right wheel
    await motor.run_for_degrees(RIGHT, 150, 400)

     #Left attachment up to lift seal to ensure it fully stands
    await motor.run_for_degrees(LEFT_ATTACHMENT, 180, 600)

    #Make a slight right turn to come away from seal with right wheel
    await motor.run_for_degrees(RIGHT, 200, -400)

    # down right attatchment
    await motor.run_for_degrees(RIGHT_ATTACHMENT, 200,275)

    # up right attatchment
    await motor.run_for_degrees(RIGHT_ATTACHMENT, 200,-300)

    #Make a left turn to to go back to 
    await motor.run_for_degrees(LEFT, 380, 400)

    #Move back towards map reveal
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,-350,0,velocity=500)

    #Make a left turn to to go back to
    await motor.run_for_degrees(LEFT, 350, 400)

    #Move back to base
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,-1400,0, velocity=800)

    #Move back to the base
    #await gyro_backward(distance=1700,speed=500)

runloop.run(main())
