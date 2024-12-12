def meter_to_kilometer(meter):
    if meter < 0:
        raise ValueError("Length cannot be negative")
    return meter / 1000

def kilometer_to_meter(kilometer):
    if kilometer < 0:
        raise ValueError("Length cannot be negative")
    return kilometer * 1000

def kilometer_to_miles(kilometer):
    if kilometer < 0:
        raise ValueError("Length cannot be negative")
    return kilometer * 0.621371

def mile_to_kilometer(mile):
    if mile < 0:
        raise ValueError("Length cannot be negative")
    return mile / 0.621371

def yard_to_meter(yard):
    if yard < 0:
        raise ValueError("Length cannot be negative")
    return yard / 1.094

def meter_to_yard(meter):
    if meter < 0:
        raise ValueError("Length cannot be negative")
    return meter * 1.094
