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
    motor.reset_relative_position(LEFT, 0)
    motion_sensor.reset_yaw(0)
    steer = 0
    while(motor.relative_position(LEFT)<=distance):
        #print(motor.relative_position(LEFT))
        error = motion_sensor.tilt_angles()[0] * -0.1
        # correction is an integer which is the negative of the error
        correction = int(error * 2)
        # print(correction)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity= (-1*speed))
    motor_pair.stop(motor_pair.PAIR_1,stop=motor.BRAKE)
    print('done')
# ----------------- Example main -----------------
async def main():
    # # prepare motors (same pattern as your sample)
    # motion_sensor.set_yaw_face(motion_sensor.FRONT)
    # motion_sensor.reset_yaw(0)
    # speed = 400
    # Yaw = motion_sensor.tilt_angles()[0] / 10.0

    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, LEFT, RIGHT)
    
    await gyro_forward(1200, 400)
    await gyro_backward(1200, 400)
