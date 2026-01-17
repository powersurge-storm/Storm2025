import runloop
from hub import motion_sensor
from hub import port
import motor_pair
import motor

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.pair(motor_pair.PAIR_1, port.B,port.D)# Define Motors

    motor_pair.unpair(motor_pair.PAIR_1) # unpairs the motors in case it conflicts with previous code
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)

#Move Forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity=840) #move forward
    await runloop.sleep_ms(2000) #waits for 2 seconds
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Left
    await runloop.sleep_ms(1000)      
    motion_sensor.reset_yaw(0)
    await motor.run_for_degrees(port.D, 600, 500) #turn left

#Solve Mission
    await motor.run_for_time(port.C, 3000, -500) # spin gear (lift the flag up)
    await runloop.sleep_ms(1500)

#Turn Right
    await motor.run_for_degrees(port.D, 610, -3000) #turn right
    # await runloop.sleep_ms(1500)

#Move Forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity= 1000)  
    await runloop.sleep_ms(1500)#waits for 2 seconds
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Left
    await motor.run_for_degrees(port.D, 200, 500) #turn left
    # await runloop.sleep_ms(1000)
 
#Go To Home Base 
    motor_pair.move(motor_pair.PAIR_1,0,velocity= 1000)
    await runloop.sleep_ms(1000)#waits for 2 seconds
    motor_pair.stop(motor_pair.PAIR_1)


    # motor_pair.move(motor_pair.PAIR_1,0,velocity= 8000)#backward move
    # motor_pair.stop(motor_pair.PAIR_1)
    # await runloop.sleep_ms(500)



runloop.run(main())
