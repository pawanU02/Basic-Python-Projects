def celsius_to_kelvin(c):
    if c < -273.15:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return k - 273.15

def celsius_to_fahrenheit(c):
    if c < -273.15:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (c * (9/5)) + 32

def fahrenheit_to_celsius(f):
    if f < -459.67:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (f - 32) * (5 / 9)

def kelvin_to_fahrenheit(k):
    if k < 0:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return 1.8 * (k - 273.15) + 32

def fahrenheit_to_kelvin(f):
    if f < -459.67:
        raise ValueError("Temperature cannot be lower than absolute zero")
    return (f + 459.67) * (5 / 9)

