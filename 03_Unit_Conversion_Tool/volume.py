def l_to_ml(l):
    """Converts liters to milliliters.

    Args:
        l (float): Volume in liters.

    Returns:
        float: Volume in milliliters.

    Raises:
        ValueError: If the input liter value is negative.
    """

    if l < 0:
        raise ValueError("Volume cannot be negative")
    return l * 1000

def ml_to_l(ml):
    """Converts milliliters to liters.

    Args:
        ml (float): Volume in milliliters.

    Returns:
        float: Volume in liters.

    Raises:
        ValueError: If the input milliliter value is negative.
    """

    if ml < 0:
        raise ValueError("Volume cannot be negative")
    return ml / 1000

def kl_to_l(kl):
    """Converts kiloliters to liters.

    Args:
        kl (float): Volume in kiloliters.

    Returns:
        float: Volume in liters.

    Raises:
        ValueError: If the input kiloliter value is negative.
    """

    if kl < 0:
        raise ValueError("Volume cannot be negative")
    return kl * 1000

def l_to_kl(l):
    """Converts liters to kiloliters.

    Args:
        l (float): Volume in liters.

    Returns:
        float: Volume in kiloliters.

    Raises:
        ValueError: If the input liter value is negative.
    """

    if l < 0:
        raise ValueError("Volume cannot be negative")
    return l / 1000

def cl_to_ml(cl):
    """Converts centiliters to milliliters.

    Args:
        cl (float): Volume in centiliters.

    Returns:
        float: Volume in milliliters.

    Raises:
        ValueError: If the input centiliter value is negative.
    """

    if cl < 0:
        raise ValueError("Volume cannot be negative")
    return cl * 10

def ml_to_cl(ml):
    """Converts milliliters to centiliters.

    Args:
        ml (float): Volume in milliliters.

    Returns:
        float: Volume in centiliters.

    Raises:
        ValueError: If the input milliliter value is negative.
    """

    if ml < 0:
        raise ValueError("Volume cannot be negative")
    return ml / 10