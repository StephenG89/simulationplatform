import numpy as np
from constants import rho_air

def aero_drag(v, a, Cd):
    fd = 0.5 * Cd * a * rho_air * v**2
    return fd
