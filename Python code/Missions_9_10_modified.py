import runloop
from hub import port
import motor_pair
from hub import motion_sensor
import motor
async def main():
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)# reset yaw angle
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)

#Move Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 300, 0, velocity=400)
 
#Turn Left
    await motor.run_for_degrees(port.D, 230, 200)

#Move Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 450, 0, velocity = 400)

#Turn Left
    await motor.run_for_degrees(port.D, 230, 200)

#Move Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 120, 0, velocity = 200)

#Drop Roof Attachment
    await motor.run_for_degrees(port.F,400,-900)

#Swing Scale Pan Attachment and Hook Into Scale Pan
    await motor.run_for_degrees(port.C, 416,-800 )

#Remove Scale Pan and Swing it Into Home Base by Swinging Scale Pan Attachment In The Opposite Direction
    await runloop.sleep_ms(500)
    await motor.run_for_degrees(port.C, 400, 400)
    
#Move Back
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 350, 0, velocity = -400)

#Lift Roof Attachment a Little So That It Doesn't Undo The Mission
    await motor.run_for_degrees (port.F, 200, 400)

#Move Forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 0, velocity = 200)

#Lift Roof Attachment
    await motor.run_for_degrees(port.F, 400,900)

#Move Forward
    await motor_pair.move_for_degrees (motor_pair.PAIR_1, 50, 0, velocity = 200 )

#Move Backwards
    await motor_pair.move_for_degrees (motor_pair.PAIR_1, 900, 0, velocity = -1000)

runloop.run(main())
