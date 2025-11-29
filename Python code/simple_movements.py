from hub import light_matrix, port
from app import sound
import motor
import motor_pair
import runloop

async def main():
    # write your code here
    #await light_matrix.write("Hi!")

    
    sound.play('Plane Flying By')
   
   

    #Setting driving motors
    motor_pair.pair(motor_pair.PAIR_1,port.B, port.D) 

    #Move fwd
    # await motor_pair.move_for_time(motor_pair.PAIR_1,1500, 0, velocity=1000,deceleration=200)
    # motor_pair.move_for_time(motor_pair.PAIR_1,1500, 0, velocity=-1000, deceleration=200)

    # Perfect movement uses acceleration and decleration, and drive with lower velocity.
    # Always use move_for_degrees, so it travels same distance everytime
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,1000, 0, velocity=1000,deceleration=500,acceleration=500)
    motor_pair.move_for_degrees(motor_pair.PAIR_1,1000, 0, velocity=-1000,deceleration=500,acceleration=500)
    sound.play('Applause 2')

 
runloop.run(main())
