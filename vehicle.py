from mechanics import aero_drag


class simpleVehicle:
    def __init__(self, afront, cdrag, gvw, ulw):
        self.afront = afront
        self.cdrag = cdrag
        self.gvw = gvw
        self.ulw = ulw

    def accel(self, v, ftrac):
        # Simple F = ma calc
        drag = aero_drag(v, self.afront, self.cdrag)
        grav = 0 # Replace with slope
        fres = ftrac - drag - grav
        acc = fres / masscalc(payload=1)
        return acc

    def masscalc(self, payload):
        mass = self.ulw + (self.gvw - self.ulw) * payload
        return mass
