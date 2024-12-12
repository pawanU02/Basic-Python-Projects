def kg_to_g(kg):
    """Converts kilograms to grams.

    Args:
        kg (float): Weight in kilograms.

    Returns:
        float: Weight in grams.

    Raises:
        ValueError: If the input kilogram value is negative.
    """

    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 1000

def g_to_kg(g):
    """Converts grams to kilograms.

    Args:
        g (float): Weight in grams.

    Returns:
        float: Weight in kilograms.

    Raises:
        ValueError: If the input gram value is negative.
    """

    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g / 1000

def g_to_mg(g):
    """Converts grams to milligrams.

    Args:
        g (float): Weight in grams.

    Returns:
        float: Weight in milligrams.

    Raises:
        ValueError: If the input gram value is negative.
    """

    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g * 1000

def mg_to_g(mg):
    """Converts milligrams to grams.

    Args:
        mg (float): Weight in milligrams.

    Returns:
        float: Weight in grams.

    Raises:
        ValueError: If the input milligram value is negative.
    """

    if mg < 0:
        raise ValueError("Weight cannot be negative")
    return mg / 1000

def lb_to_kg(lb):
    """Converts pounds to kilograms.

    Args:
        lb (float): Weight in pounds.

    Returns:
        float: Weight in kilograms.

    Raises:
        ValueError: If the input pound value is negative.
    """

    if lb < 0:
        raise ValueError("Weight cannot be negative")
    return lb * 0.453592

def kg_to_lb(kg):
    """Converts kilograms to pounds.

    Args:
        kg (float): Weight in kilograms.

    Returns:
        float: Weight in pounds.

    Raises:
        ValueError: If the input kilogram value is negative.
    """

    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg / 0.453592