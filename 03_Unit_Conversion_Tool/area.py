def square_meter_to_square_kilometer(square_meter):
    if square_meter < 0:
        raise ValueError("Area cannot be negative")
    return square_meter / 1_000_000

def square_kilometer_to_square_meter(square_kilometer):
    if square_kilometer < 0:
        raise ValueError("Area cannot be negative")
    return square_kilometer * 1_000_000

def acre_to_square_foot(acre):
    if acre < 0:
        raise ValueError("Area cannot be negative")
    return acre * 43_560

def square_foot_to_acre(square_foot):
    if square_foot < 0:
        raise ValueError("Area cannot be negative")
    return square_foot / 43_560

def hectare_to_square_meter(hectare):
    if hectare < 0:
        raise ValueError("Area cannot be negative")
    return hectare * 10_000

def square_meter_to_hectare(square_meter):
    if square_meter < 0:
        raise ValueError("Area cannot be negative")
    return square_meter / 10_000