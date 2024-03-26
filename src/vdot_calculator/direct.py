# pylint: disable=C0114
import math


def direct(time_minutes: float, total_distance: float) -> float:
    """
    Calculate the VO2max using the Daniels Method.

    Parameters:
    - time_minutes (float): The total running time in minutes.
    - total_distance (float): The total running distance in meters.

    Returns:
    - float: The calculated VO2max.
    """
    velocity = total_distance / time_minutes
    percent_max = (
        0.8
        + 0.1894393 * math.e ** (-0.012778 * time_minutes)
        + 0.2989558 * math.e ** (-0.1932605 * time_minutes)
    )
    vo2 = -4.60 + 0.182258 * velocity + 0.000104 * velocity**2
    vo2max = vo2 / percent_max
    return vo2max
