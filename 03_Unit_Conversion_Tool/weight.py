def kg_to_g(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 1000

def g_to_kg(g):
    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g / 1000

def g_to_mg(g):
    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g * 1000

def mg_to_g(mg):
    if mg < 0:
        raise ValueError("Weight cannot be negative")
    return mg / 1000

def lb_to_kg(lb):
    if lb < 0:
        raise ValueError("Weight cannot be negative")
    return lb * 0.456

def kg_to_lb(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg / 0.456

