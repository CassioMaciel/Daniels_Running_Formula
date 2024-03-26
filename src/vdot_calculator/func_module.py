"""
vdot_calculator Module

This module provides functions for calculating VDOT (Volume of Oxygen)
values based on the original Jack Danniels Running Formula.
bibliografy:
https://www.letsrun.com/forum/flat_read.php?thread=3704747
https://www.letsrun.com/forum/flat_read.php?thread=4858970

Usage:
>>> import datetime
>>> import vdot_calculator as vdot
>>> time = datetime.time(minute=27, second=00)
>>> distance = 5000 # meters
>>> vdot.vdot_from_time_and_distance(time, distance)
34.96321966414413

>>> import datetime
>>> import vdot_calculator as vdot
>>> pace = datetime.time(minute=5, second=24)
>>> distance = 5000 # meters
>>> vdot.vdot_from_distance_and_pace(distance,pace)
34.96321966414413

>>> import datetime
>>> import vdot_calculator as vdot
>>> pace = datetime.time(minute=5, second=24)
>>> time = datetime.time(minute=27, second=00)
>>> vdot.vdot_from_time_and_pace(time,pace)
34.96321966414413
"""
