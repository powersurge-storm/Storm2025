# Python basics code
# Author: PowerSurge Storm students of 2025
# Kid-friendly gyro drive & turn helpers for SPIKE Prime (official API style)
#
# Uses the same imports and modules as your sample code:
#
# import runloop
# import hub
# from hub import port
# import motor_pair
# from hub import motion_sensor
# import motor
# import color_sensor
# import color
#
# Assumptions:
# - Drive motors are on ports B (left) and D (right) and are paired as motor_pair.PAIR_1
# - motion_sensor.tilt_angles()[0] returns yaw in tenths of degrees (so 900 == 90°)
# - We use small, easy-to-read loops so kids can understand and change things

import runloop
import hub
from hub import port
import motor_pair
from hub import motion_sensor
import motor
import asyncio    # runloop supports async style used in your sample

# helper: keep angle between -180 and +180 degrees
def short_angle_deg(a):
    return (a + 180) % 360 - 180

# ---------- Drive straight (chunked, simple & safe for kids) ----------
# Break the big wheel movement into small pieces and correct heading between pieces.
async def drive_straight_gyro(total_degrees=1300,
                              chunk_degrees=20,
                              velocity=400,
                              Kp=0.5):
    """
    Drive approximately total_degrees of wheel rotation while using the gyro to stay straight.
    - total_degrees: how far the wheels should turn in total (like your original 1300)
    - chunk_degrees: how many wheel degrees per small step (smaller = smoother)
    - velocity: motor speed (0..600)
    - Kp: how strongly we correct when we drift (try 0.3 - 0.8)
    """
    # Make sure gyro faces forward and reset yaw so current heading = 0
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

    steps = total_degrees // chunk_degrees
    remainder = total_degrees % chunk_degrees

    for _ in range(steps):
        # read yaw in degrees (tilt_angles()[0] is tenths of degrees)
        yaw_tenths = motion_sensor.tilt_angles()[0]
        yaw = yaw_tenths / 10.0
        error = short_angle_deg(yaw - 0)          # how far from straight (degrees)
        steering = Kp * error                     # steering value to give to motor_pair

        # clamp steering to allowed range
        if steering > 100:
            steering = 100
        if steering < -100:
            steering = -100

        # move a small chunk while applying steering
        await motor_pair.move_for_degrees(motor_pair.PAIR_1,
                                         chunk_degrees,
                                         int(steering),
                                         velocity=velocity)

    # leftover degrees
    if remainder:
        yaw = motion_sensor.tilt_angles()[0] / 10.0
        error = short_angle_deg(yaw - 0)
        steering = int(max(min(Kp * error, 100), -100))
        await motor_pair.move_for_degrees(motor_pair.PAIR_1,
                                         remainder,
                                         steering,
                                         velocity=velocity)

# ---------- Spin turn (turn on the spot) ----------
# Uses motor_pair.move() like your sample to keep code very simple for kids.
async def spin_turn(angle_deg, speed=150, slow_down_at=20):
    """
    Spin turn in place (both wheels move to turn on the spot).
    - angle_deg: positive = turn right, negative = turn left (degrees)
    - speed: how fast to turn (try 100-300)
    - slow_down_at: how many degrees before target to start slowing
    Example: await spin_turn(90)  # spin right 90 degrees
    """
    if angle_deg == 0:
        return

    # prepare gyro
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

    # motion_sensor.tilt_angles()[0] is in tenths of degrees:
    target_tenths = -int(angle_deg * 10)   # mapping: turning right makes tilt go negative
    move_speed = speed if angle_deg > 0 else -speed

    # loop until we reach (or pass) the target
    while True:
        cur = motion_sensor.tilt_angles()[0]
        # distance remaining in tenths of degrees (positive value)
        remaining = abs(target_tenths - cur)

        # stop when we've reached or passed the target
        if (angle_deg > 0 and cur <= target_tenths) or (angle_deg < 0 and cur >= target_tenths):
            break

        # slow down when near the target to avoid big overshoot
        if remaining < slow_down_at * 10:
            # reduce speed proportionally but not below a small minimum
            scaled = max(40, int(abs(speed) * (remaining / (slow_down_at * 10))))
            move_speed = scaled if angle_deg > 0 else -scaled
        else:
            move_speed = speed if angle_deg > 0 else -speed

        # simple move call like your sample (keeps the API easy)
        motor_pair.move(motor_pair.PAIR_1, move_speed)

        # small sleep so other system tasks run and to read gyro again
        await asyncio.sleep(0.02)

    motor_pair.stop(motor_pair.PAIR_1)

# ---------- Pivot turn (one wheel stays still) ----------
# We run the moving wheel a little at a time until the gyro shows we turned enough.
async def pivot_turn(angle_deg, pivot_side='right', speed=180, slow_down_at=20, chunk_degrees=8):
    """
    Pivot turn: one wheel stays still, the other moves.
    - pivot_side: 'right' or 'left' (which wheel does NOT move)
    - angle_deg: positive = turn right, negative = turn left
    - speed: speed for the moving wheel (try 120-250)
    - chunk_degrees: how many degrees the moving motor turns per small step
    Example: await pivot_turn(90, pivot_side='right')
    """
    if angle_deg == 0:
        return

    # Ports: we assume left motor is on port.B and right motor on port.D
    LEFT_PORT = port.B
    RIGHT_PORT = port.D

    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

    target_tenths = -int(angle_deg * 10)   # using same sign convention as spin_turn

    # Which motor will move?
    if pivot_side == 'right':
        moving_port = LEFT_PORT   # pivot around right wheel -> left motor moves
        # For turning right (angle_deg>0) left motor runs forward (positive). For left turn negative.
        direction = 1 if angle_deg > 0 else -1
    else:
        moving_port = RIGHT_PORT  # pivot around left wheel -> right motor moves
        direction = 1 if angle_deg < 0 else -1  # flipping because moving right motor forward can cause left turn

    while True:
        cur = motion_sensor.tilt_angles()[0]
        if (angle_deg > 0 and cur <= target_tenths) or (angle_deg < 0 and cur >= target_tenths):
            break

        remaining = abs(target_tenths - cur)
        if remaining < slow_down_at * 10:
            cur_speed = max(40, int(abs(speed) * (remaining / (slow_down_at * 10))))
        else:
            cur_speed = abs(speed)

        cur_speed = cur_speed * (1 if direction > 0 else -1)

        # move the single motor a small chunk (runs while we await)
        await motor.run_for_degrees(moving_port, chunk_degrees * (1 if direction > 0 else -1), cur_speed)

        # small pause so we re-check gyro and can slow down
        await asyncio.sleep(0.01)

    # ensure pair is stopped (safety)
    try:
        motor_pair.stop(motor_pair.PAIR_1)
    except Exception:
        pass

# ---------- Example main showing multiple calls ----------
async def main():
    # set up motors like your sample (unpair then pair to known ports)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, port.B, port.D)

    # Drive straight a bit with gyro corrections
    await drive_straight_gyro(total_degrees=800, chunk_degrees=20, velocity=350, Kp=0.5)

    # Spin right 90 degrees
    await spin_turn(90, speed=160)

    # Drive a short distance
    await drive_straight_gyro(total_degrees=300, chunk_degrees=15, velocity=300, Kp=0.5)

    # Pivot left 45 degrees around left wheel
    await pivot_turn(-45, pivot_side='left', speed=160)

    # Another spin right 90 to show multiple calls in a row
    await spin_turn(90, speed=160)

# run the program
runloop.run(main())