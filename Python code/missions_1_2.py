# Author(s): Anavi Sambaraju & Sharman Gokhale
# Team Powersurge Storm 2025
# This code solves 2 missions Surface Brushing & Map Reveal, and scores 60 points

from hub import port
import motor_pair
from hub import motion_sensor
import motor
import runloop

async def main():
   motion_sensor.set_yaw_face(motion_sensor.FRONT)
   motion_sensor.reset_yaw(0)
   motor_pair.unpair(motor_pair.PAIR_1)
   motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)

   motor_pair.move(motor_pair.PAIR_1,0,velocity=847)
   await runloop.sleep_ms(1770)
   motor_pair.stop(motor_pair.PAIR_1)
   motion_sensor.reset_yaw(0)# reset yaw angle  
   await runloop.sleep_ms(1770)

   await motor.run_for_degrees(port.D,200, 300)
   motor.stop(port.D)

   motor_pair.move(motor_pair.PAIR_1,0,velocity=180)
   await runloop.sleep_ms(1770)
   motor_pair.stop(motor_pair.PAIR_1)
   motion_sensor.reset_yaw(0)# reset yaw angle

   #Lift right atatchment up

   await motor.run_for_degrees(port.F,-270,300)
   motor.stop(port.F)

   motor_pair.move(motor_pair.PAIR_1,0,velocity=-180)
   await runloop.sleep_ms(1270)
   motor_pair.stop(motor_pair.PAIR_1)
   motion_sensor.reset_yaw(0)# reset yaw angle

   #Turn back toward base using right wheel
   await motor.run_for_degrees(port.D,-230,300)
   motor.stop(port.D)

   #Move back to align with rubberband attachment
   await motor_pair.move_for_degrees(motor_pair.PAIR_1,-300, 0)
   
   #waiting for 2 sec before the rubberband attachment move
   await runloop.sleep_ms(2000)

   await motor.run_for_degrees(port.C,-400,500)
   motor.stop(port.C)

   await motor.run_for_degrees(port.C, 400,500)
   motor.stop(port.C)

   motor_pair.move(motor_pair.PAIR_1,0,velocity=-800)
   await runloop.sleep_ms(1770)
   motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())

