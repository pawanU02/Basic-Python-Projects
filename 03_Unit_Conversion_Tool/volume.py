def l_to_ml(l):
    if l < 0:
        raise ValueError("Volume cannot be negative")
    return l * 1000

def ml_to_l(ml):
    if ml < 0:
        raise ValueError("Volume cannot be negative")
    return ml / 1000

def kl_to_l(kl):
    if kl < 0:
        raise ValueError("Volume cannot be negative")
    return kl * 1000

def l_to_kl(l):
    if l < 0:
        raise ValueError("Volume cannot be negative")
    return l / 1000

def cl_to_ml(cl):
    if cl < 0:
        raise ValueError("Volume cannot be negative")
    return cl * 10

def ml_to_cl(ml):
    if ml < 0:
        raise ValueError("Volume cannot be negative")
    return ml / 10


