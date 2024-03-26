# pylint: disable=C0114
import datetime
import math
from .direct import direct


def pace_marathon(v_dot: float) -> datetime.time:
    """
    Calculate the running pace corresponding to the given VDOT for a marathon.

    Args:
    - v_dot (float): The VDOT value for which to calculate the running pace.

    Returns:
    - datetime.time: The calculated running pace represented as a time object.
    """
    continue_criteria = True
    index = 0.0
    t_min = 50.0
    v_dot_min = direct(t_min, 42195)
    t_max = 360.0
    t_med = (t_min + t_max) / 2
    v_dot_max = direct(t_max, 42195)
    while continue_criteria:
        index += 1
        t_med = (t_min + t_max) / 2
        v_dot_med = direct(t_med, 42195)
        error = v_dot_med - v_dot
        if error / (v_dot_max-v_dot) > 0:
            t_max = t_med
            v_dot_max = v_dot_med
        elif error / (v_dot_min-v_dot) > 0:
            t_min = t_med
            v_dot_min = v_dot_med
        if abs(error) < 0.01:
            continue_criteria = False
        if index > 400:
            print('WARNING: doesn\'t solve')
            continue_criteria = False

    pace_minutes = t_med/42.195
    minutes = int(math.floor(pace_minutes))
    seconds = int(math.floor((pace_minutes-minutes)*60))
    output = datetime.time(
                       minute=minutes,
                       second=seconds)

    return output
