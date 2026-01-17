# import runloop                                                             
from hub import port                                                              
import motor_pair
from hub import motion_sensor
import motor
import runloop

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D) #creating new pair motors at        this whole chunk from 9 to 14 is to activate the driving motors and reseting the bot to move smoothly

#  #Move Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,1400,0,velocity=600) 
    await motor.run_for_degrees(port.C,100, -200)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,1400,0,velocity=-600)


runloop.run(main())
