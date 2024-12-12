def meter_to_kilometer(meter):
    """Converts meters to kilometers.

    Args:
        meter (float): The distance in meters.

    Returns:
        float: The distance in kilometers.

    Raises:
        ValueError: If the input meter value is negative.
    """

    if meter < 0:
        raise ValueError("Length cannot be negative")
    return meter / 1000

def kilometer_to_meter(kilometer):
    """Converts kilometers to meters.

    Args:
        kilometer (float): The distance in kilometers.

    Returns:
        float: The distance in meters.

    Raises:
        ValueError: If the input kilometer value is negative.
    """

    if kilometer < 0:
        raise ValueError("Length cannot be negative")
    return kilometer * 1000

def kilometer_to_miles(kilometer):
    """Converts kilometers to miles.

    Args:
        kilometer (float): The distance in kilometers.

    Returns:
        float: The distance in miles.

    Raises:
        ValueError: If the input kilometer value is negative.
    """

    if kilometer < 0:
        raise ValueError("Length cannot be negative")
    return kilometer * 0.621371

def mile_to_kilometer(mile):
    """Converts miles to kilometers.

    Args:
        mile (float): The distance in miles.

    Returns:
        float: The distance in kilometers.

    Raises:
        ValueError: If the input mile value is negative.
    """

    if mile < 0:
        raise ValueError("Length cannot be negative")
    return mile / 0.621371

def yard_to_meter(yard):
    """Converts yards to meters.

    Args:
        yard (float): The distance in yards.

    Returns:
        float: The distance in meters.

    Raises:
        ValueError: If the input yard value is negative.
    """

    if yard < 0:
        raise ValueError("Length cannot be negative")
    return yard / 1.094

def meter_to_yard(meter):
    """Converts meters to yards.

    Args:
        meter (float): The distance in meters.

    Returns:
        float: The distance in yards.

    Raises:
        ValueError: If the input meter value is negative.
    """

    if meter < 0:
        raise ValueError("Length cannot be negative")
    return meter * 1.094