import runloop
from hub import port
import motor_pair
from hub import motion_sensor
import motor
# from types import MethodDescriptorType

async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)
    motor_pair.unpair (motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)

#Move Forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity=400)
    await runloop.sleep_ms(1500)
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Left
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]<940:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,-100)#move to left
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

#Move M9 Attachment Up
    motor.run(port.F, -250,acceleration=100)
    await runloop.sleep_ms(2000)
    motor.stop(port.F)

# Move Forward
    motor_pair.move(motor_pair.PAIR_1,0,velocity=467)
    await runloop.sleep_ms(1800)
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Right
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]>-940:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100)#move to right
    motor_pair.stop(motor_pair.PAIR_1)#stop motor

#Move Forwards
    motor_pair.move(motor_pair.PAIR_1,0,velocity=132)
    await runloop.sleep_ms(400)
    motor_pair.stop(motor_pair.PAIR_1)

    #Use M10 Attatchment-
    motor.run(port.C, -110,acceleration=120)
    await runloop.sleep_ms(3500)
    motor.stop(port.C)
    await runloop.sleep_ms(1800)

#Move Backwards
    motor_pair.move(motor_pair.PAIR_1,0,velocity=-132)
    await runloop.sleep_ms(1500)
    motor_pair.stop(motor_pair.PAIR_1)

#Turn Left
    motion_sensor.reset_yaw(0)# reset yaw angle
    while motion_sensor.tilt_angles()[0]<940:#getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,-100)#move to left
    motor_pair.stop(motor_pair.PAIR_1)#stop

#Return to Home Base Step 1
    motor_pair.move(motor_pair.PAIR_1,0,velocity=-400)
    await runloop.sleep_ms(3000)
    motor_pair.stop(motor_pair.PAIR_1)

#Return to Home Base Step 2
    motor_pair.move(motor_pair.PAIR_1,0,velocity=-132)
    await runloop.sleep_ms(1500)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
