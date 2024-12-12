def celsius_to_kelvin(c):
    """Converts Celsius to Kelvin.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if c < -273.15:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return c + 273.15

def kelvin_to_celsius(k):
    """Converts Kelvin to Celsius.

    Args:
        k (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Celsius.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if k < 0:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return k - 273.15

def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if c < -273.15:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (c * (9/5)) + 32

def fahrenheit_to_celsius(f):
    """Converts Fahrenheit to Celsius.

    Args:
        f (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if f < -459.67:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (f - 32) * (5 / 9)

def kelvin_to_fahrenheit(k):
    """Converts Kelvin to Fahrenheit.

    Args:
        k (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if k < 0:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return 1.8 * (k - 273.15) + 32

def fahrenheit_to_kelvin(f):
    """Converts Fahrenheit to Kelvin.

    Args:
        f (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Kelvin.

    Raises:
        ValueError: If the temperature is below absolute zero.
    """

    if f < -459.67:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (f + 459.67) * (5 / 9)