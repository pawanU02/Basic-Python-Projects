def second_to_minute(s):
    """Converts seconds to minutes.

    Args:
        s (float): The time in seconds.

    Returns:
        float: The time in minutes.

    Raises:
        ValueError: If the input second value is negative.
    """

    if s < 0:
        raise ValueError("Time cannot be negative")
    return s / 60

def minute_to_second(m):
    """Converts minutes to seconds.

    Args:
        m (float): The time in minutes.

    Returns:
        float: The time in seconds.

    Raises:
        ValueError: If the input minute value is negative.
    """

    if m < 0:
        raise ValueError("Time cannot be negative")
    return m * 60

def minute_to_hour(m):
    """Converts minutes to hours.

    Args:
        m (float): The time in minutes.

    Returns:
        float: The time in hours.

    Raises:
        ValueError: If the input minute value is negative.
    """

    if m < 0:
        raise ValueError("Time cannot be negative")
    return m / 60

def hour_to_minute(h):
    """Converts hours to minutes.

    Args:
        h (float): The time in hours.

    Returns:
        float: The time in minutes.

    Raises:
        ValueError: If the input hour value is negative.
    """

    if h < 0:
        raise ValueError("Time cannot be negative")
    return h * 60

def second_to_hour(s):
    """Converts seconds to hours.

    Args:
        s (float): The time in seconds.

    Returns:
        float: The time in hours.

    Raises:
        ValueError: If the input second value is negative.
    """

    if s < 0:
        raise ValueError("Time cannot be negative")
    return s / 3600

def hour_to_second(h):
    """Converts hours to seconds.

    Args:
        h (float): The time in hours.

    Returns:
        float: The time in seconds.

    Raises:
        ValueError: If the input hour value is negative.
    """

    if h < 0:
        raise ValueError("Time cannot be negative")
    return h * 3600