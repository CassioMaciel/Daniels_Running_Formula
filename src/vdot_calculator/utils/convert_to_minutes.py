# pylint: disable=C0114
import datetime


def convert_to_minutes(time: datetime.time) -> float:
    """
    Convert a time value to minutes.

    Parameters:
    - time (datetime.time): The time value to be converted.

    Returns:
    - float: The time value in minutes.
    """
    time_minutes = time.minute + time.second / 60 + time.hour * 60
    return time_minutes
