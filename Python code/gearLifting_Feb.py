# Author(s): Vihaan Cheepurupalli & Sana Salavath
# Team Powersurge Storm 2025
# This code solves 1 mission Angler Artifact and sends Robot to Left base without losing a precision token

import runloop
from hub import motion_sensor
from hub import port
import motor_pair
import motor

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle

    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)

    print(motion_sensor.tilt_angles()[0])

#Move Forward (on the way to solve mission)
    motor_pair.move(motor_pair.PAIR_1,0,velocity=840) #move forward
    await runloop.sleep_ms(2000) #waits for 2 seconds
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Left for robot to face the mission 
    await runloop.sleep_ms(1000)      
    motion_sensor.reset_yaw(0)
    await motor.run_for_degrees(port.D, 600, 500) #turn left to solve mission

#Solve Mission to lift angler artifact 
    await motor.run_for_time(port.C, 2000, -500) # spin gear (lift the flag up)
    await runloop.sleep_ms(1500)

    print(motion_sensor.tilt_angles()[0])

    while(motion_sensor.tilt_angles()[0]>-60):
        motor.run(port.D,-300)
    motor.stop(port.D)

    print(motion_sensor.tilt_angles()[0])



#Turn Right (turns to go to left home base)
   # await motor.run_for_degrees(port.D, 610, -3000) #turn right(turns to go to base)
    # await runloop.sleep_ms(1500)

#Move Forward (reaches left home base)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,2200, -5,velocity= 1000) #goes to base on left side 


runloop.run(main())
