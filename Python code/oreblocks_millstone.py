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
    motion_sensor.reset_yaw(0)
    while motion_sensor.tilt_angles()[0]>-380:
     motor_pair.move(motor_pair.PAIR_1,100)
    motor_pair.stop(motor_pair.PAIR_1)

    #drop attachment 
    motor.run(port.F, -320,acceleration=100000)
    await runloop.sleep_ms(1000)
    motor.stop(port.F)

    #move forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity= 50)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)

    #pick up attachment
    motor.run(port.F, 200,acceleration=1000)
    await runloop.sleep_ms(1000)
    motor.stop(port.F)

    #Go back 
    motor_pair.move(motor_pair.PAIR_1,0,velocity= -50)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)

    #Drop other attachment 
    motor.run(port.C, 350,acceleration=100000)
    await runloop.sleep_ms(1000)
    motor.stop(port.C)

    #move left
    while motion_sensor.tilt_angles()[0]< 150:
        motor_pair.move(motor_pair.PAIR_1,-100)
    motor_pair.stop(motor_pair.PAIR_1)

    #move forward 
    motor_pair.move(motor_pair.PAIR_1,0,velocity= 20)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)

    # Another Turn Left to solve Markets
    while motion_sensor.tilt_angles()[0]< 150:
        motor_pair.move(motor_pair.PAIR_1,-100)
    motor_pair.stop(motor_pair.PAIR_1)

    # Turn Right back
    while motion_sensor.tilt_angles()[0]>-150:
        motor_pair.move(motor_pair.PAIR_1,100)
    motor_pair.stop(motor_pair.PAIR_1)

    #Go back to Home base
    motor_pair.move(motor_pair.PAIR_1,0,velocity= -670)
    await runloop.sleep_ms(2150)
    motor_pair.stop(motor_pair.PAIR_1)


runloop.run(main())
