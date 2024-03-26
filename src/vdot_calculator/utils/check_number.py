# pylint: disable=C0114
def check_number(value) -> float:
    """
    Checks if the input value is numeric and returns it as a float.

    Parameters:
    - value: Numeric value to be checked and converted to float.

    Returns:
    - float: Converted numeric value.

    Raises:
    - TypeError: If the input is not numeric (neither int nor float).
    """
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except (ValueError, TypeError):
            pass

    raise TypeError(
        'The input should be of numeric type, either int or float.'
    )
