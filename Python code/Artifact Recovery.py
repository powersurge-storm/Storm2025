import runloop
from hub import port
import motor_pair
from hub import motion_sensor
import motor

LEFT = port.B
RIGHT = port.D
LEFT_ATTACHMENT = port.C
RIGHT_ATTACHMENT = port.F

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

async def gyro_backward(distance, speed):
    motion_sensor.reset_yaw(0)
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

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,LEFT,RIGHT) #creating new pair motors at        this whole chunk from 9 to 14 is to activate the driving motors and reseting the bot to move smoothly

    # *****Code for this run starts here *****
    await motor.run_for_degrees(port.C,300,600)
    motor.run_for_degrees(port.F,500,600 )

    # Move forward to hit the wall
    await gyro_forward(distance=1900,speed=800)
     
     #move back from wall
    await gyro_backward(distance=125, speed=100)    
    
    #Make a right turn to align with Mineshaft using left wheel
    await motor.run_for_degrees(LEFT, 440, -350)

    await gyro_backward(distance=75, speed=50)

    await motor.run_for_degrees(port.C, 300,-600)
    motor.run_for_degrees(port.F, 400,-600)

    
    await gyro_forward(distance=315,speed=125)
    #lift artifact and send mineshaft
    await motor.run_for_degrees(port.C, 70, 475)
    motor.run_for_degrees(port.F, 500, 950)
    
    
    await gyro_backward(distance=150,speed=220)


    await motor.run_for_degrees(port.F,300,600)

    await motor.run_for_degrees(port.C,40,200)


    await gyro_backward(distance=250,speed=200)

    await motor.run_for_degrees(port.C,150,400)

    await gyro_forward(distance=100,speed=400)

    #Turn slightly towards base to give turning room
    await motor.run_for_degrees(LEFT, 200, 400)

    #Turn slightly towards Seal
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,250, 400,-400)

    #Move to Seal
    await gyro_forward(distance=600,speed=600)

    #Attachment down for Seal
    await motor.run_for_degrees(port.F,350,-500)

    #Sneak under Seal
    await gyro_forward(distance=300,speed=300)

    #Lift for Seal
    await motor.run_for_degrees(port.F,120, 600)

    #Turn slightly Seal
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,150, -300,300)

    #Lift for Seal
    await motor.run_for_degrees(port.F,200, 600)

    #Move to away from seal
    await gyro_backward(distance=100,speed=400)

    #Turn to drop artifact
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,300, 300,-300)

    #Drop artifact
    await motor.run_for_degrees(port.C,200,-400)









runloop.run(main())
