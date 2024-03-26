# pylint: disable=C0114
import datetime
from .utils import (
    check_time,
    check_number,
    convert_to_minutes)
from .direct import direct


def vdot_from_time_and_distance(time: datetime.time, distance: float) -> float:
    """
    Calculate VDOT from time and distance.

    Parameters:
    - time (datetime.time): The time value of the run.
    - distance (float): The distance value of the run in meters.

    Returns:
    - float: The calculated VDOT value.
    """
    time = check_time(time)
    distance = check_number(distance)
    time_minutes = convert_to_minutes(time)
    vdot = direct(time_minutes, distance)
    return vdot
