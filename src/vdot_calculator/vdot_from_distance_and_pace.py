# pylint: disable=C0114
import datetime
from .direct import direct
from .utils import (
    check_number,
    check_time,
    convert_to_minutes,
)


def vdot_from_distance_and_pace(distance: float, pace: datetime.time) -> float:
    """
    Calculate VDOT from distance and pace.

    Parameters:
    - distance (float): The distance value of the run in meters.
    - pace (datetime.time): The pace value of the run.

    Returns:
    - float: The calculated VDOT value.
    """

    pace = check_time(pace)
    distance = check_number(distance)
    pace_minutes = convert_to_minutes(pace)
    total_time = distance * pace_minutes / 1000  # transforms distance from
    # km to meters
    vdot = direct(total_time, distance)
    return vdot
