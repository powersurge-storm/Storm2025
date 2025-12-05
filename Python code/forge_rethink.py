# Author(s): Saanvika & Darshan
# Team Powersurge Storm 2025
# This code solves 3 missions Forge, Ore Blocks, and Who lived there, and scores 90 points in one run

import runloop
from hub import port
from hub import motion_sensor
import motor_pair
import motor
async def main():

    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1, port.B,port.D)
    motor_pair.unpair(motor_pair.PAIR_1)

#forward movement
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)
    motor_pair.move( motor_pair.PAIR_1,0,velocity= 670)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)

# turn right
    # motion_sensor.reset_yaw(0)
    # while motion_sensor.tilt_angles()[0]>-380:
    #     motor_pair.move(motor_pair.PAIR_1,100)
    # motor_pair.stop(motor_pair.PAIR_1)

    await motor.run_for_degrees(port.B, -260, 300)

    #drop attachment
    motor.run(port.F, -250,acceleration=100000)
    await runloop.sleep_ms(1000)
    motor.stop(port.F)

    #move forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity= 50)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)

    #pick up attachment
    motor.run(port.F, 220,acceleration=1000)
    await runloop.sleep_ms(1000)
    motor.stop(port.F)

    #Go back
    # motor_pair.move(motor_pair.PAIR_1,0,velocity= -100)
    # await runloop.sleep_ms(1500)
    # motor_pair.stop(motor_pair.PAIR_1)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1,-200,0)

    #move left to solve 2 other missions
    await motor.run_for_degrees(port.D,600,300)

    # Solved 2nd mission

     #move right to go home
    await motor.run_for_degrees(port.D,-200,300)
    

    # #Go back to Home base
    # motor_pair.move(motor_pair.PAIR_1,0,velocity= -800)
    # await runloop.sleep_ms(2150)
    # motor_pair.stop(motor_pair.PAIR_1)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,-1600,8, velocity=500)



runloop.run(main())
