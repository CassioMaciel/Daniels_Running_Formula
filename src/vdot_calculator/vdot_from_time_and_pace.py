# pylint: disable=C0114
import datetime
from .utils import (
    check_time,
    convert_to_minutes
)
from .direct import direct

def vdot_from_time_and_pace(time: datetime.time, pace: datetime.time) -> float:
    """
    Calculate VDOT from time and pace.

    Parameters:
    - time (datetime.time): The time value of the run.
    - pace (datetime.time): The pace value of the run.

    Returns:
    - float: The calculated VDOT value.
    """
    time = check_time(time)
    pace = check_time(pace)
    time_minutes = convert_to_minutes(time)
    pace_minutes = convert_to_minutes(pace)
    distance = time_minutes / pace_minutes * 1000
    v_dot = direct(time_minutes, distance)
    return v_dot
