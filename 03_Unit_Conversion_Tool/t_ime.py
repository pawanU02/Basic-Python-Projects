def second_to_minute(s):
    if s < 0:
        raise ValueError("Time cannot be negative")
    return s / 60

def minute_to_second(m):
    if m < 0:
        raise ValueError("Time cannot be negative")
    return m * 60

def minute_to_hour(m):
    if m < 0:
        raise ValueError("Time cannot be negative")
    return m / 60

def hour_to_minute(h):
    if h < 0:
        raise ValueError("Time cannot be negative")
    return h * 60

def second_to_hour(s):
    if s < 0:
        raise ValueError("Time cannot be negative")
    return s / 3600

def hour_to_second(h):
    if h < 0:
        raise ValueError("Time cannot be negative")
    return h * 3600

