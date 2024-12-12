def square_meter_to_square_kilometer(square_meter):
    """Converts a square meter value to square kilometers.

    Args:
        square_meter (float): The area in square meters.

    Returns:
        float: The area in square kilometers.

    Raises:
        ValueError: If the input square meter value is negative.
    """

    if square_meter < 0:
        raise ValueError("Area cannot be negative")
    return square_meter / 1_000_000

def square_kilometer_to_square_meter(square_kilometer):
    """Converts a square kilometer value to square meters.

    Args:
        square_kilometer (float): The area in square kilometers.

    Returns:
        float: The area in square meters.

    Raises:
        ValueError: If the input square kilometer value is negative.
    """

    if square_kilometer < 0:
        raise ValueError("Area cannot be negative")
    return square_kilometer * 1_000_000

def acre_to_square_foot(acre):
    """Converts an acre value to square feet.

    Args:
        acre (float): The area in acres.

    Returns:
        float: The area in square feet.

    Raises:
        ValueError: If the input acre value is negative.
    """

    if acre < 0:
        raise ValueError("Area cannot be negative")
    return acre * 43_560

def square_foot_to_acre(square_foot):
    """Converts a square foot value to acres.

    Args:
        square_foot (float): The area in square feet.

    Returns:
        float: The area in acres.

    Raises:
        ValueError: If the input square foot value is negative.
    """

    if square_foot < 0:
        raise ValueError("Area cannot be negative")
    return square_foot / 43_560

def hectare_to_square_meter(hectare):
    """Converts a hectare value to square meters.

    Args:
        hectare (float): The area in hectares.

    Returns:
        float: The area in square meters.

    Raises:
        ValueError: If the input hectare value is negative.
    """

    if hectare < 0:
        raise ValueError("Area cannot be negative")
    return hectare * 10_000

def square_meter_to_hectare(square_meter):
    """Converts a square meter value to hectares.

    Args:
        square_meter (float): The area in square meters.

    Returns:
        float: The area in hectares.

    Raises:
        ValueError: If the input square meter value is negative.
    """

    if square_meter < 0:
        raise ValueError("Area cannot be negative")
    return square_meter / 10_000