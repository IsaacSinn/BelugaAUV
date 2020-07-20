
import numpy as np
import math

#constants
sin = math.sin(math.radians(45))
CG = np.array((0, 0, 0))
horizontalDist = [sin,sin,0] # FR x,y,z unit:m
verticalDist = [1,0,1] # TF x,y,z unit:m

FLposition = np.array((-horizontalDist[0], horizontalDist[1], horizontalDist[2]))
FRposition = np.array((horizontalDist[0], horizontalDist[1], horizontalDist[2])) # position x,y,z
BLposition = np.array((-horizontalDist[0], -horizontalDist[1], horizontalDist[2]))
BRposition = np.array((horizontalDist[0], -horizontalDist[1], horizontalDist[2]))
TLposition = np.array((verticalDist[0], verticalDist[1], verticalDist[2]))
TRposition = np.array((-verticalDist[0], verticalDist[1], verticalDist[2]))

FLthrust = np.array((sin, sin, 0))
FRthrust = np.array((-sin, sin, 0)) # thrust direction
BLthrust = np.array((sin, -sin, 0))
BRthrust = np.array((-sin, -sin, 0))
TLthrust = np.array((0, 0, 1))
TRthrust = np.array((0, 0, 1))

def thrusterPreset(absPosition, thrustDirect):
    position = np.subtract(absPosition, CG)
    torque = np.cross(position, thrustDirect)
    return np.concatenate((thrustDirect, torque)).reshape(6,1)

class FormulaApply(Module):
    def __init__ (self, max_percentage, formula_modifier = 30, Activate = 'A'):
        pub.subscribe(self.movementListener, 'movement')
        pub.subscribe(self.profileListener, 'profile')
        self.max_percentage = int(max_percentage)/100
        self.formula_modifier = float(formula_modifier)
        self.activate = activate
        self.profile_change = 'A'

    def run(self):
        pass

    def movementListener(self,arg1):
        if self.profile_change == self.activate:

            StrafePower, DrivePower, YawPower, Updown, Tilt_L, Tilt_R = arg1
            StrafePower = PowerFunction(StrafePower, self.formula_modifier)
            DrivePower = PowerFunction(DrivePower, self.formula_modifier)
            YawPower = PowerFunction(YawPower, self.formula_modifier)
            UpdownPower = PowerFunction(Updown, self.formula_modifier)
            Tilt_L_Power = PowerFunction(Tilt_F, self.formula_modifier)
            Tilt_R_Power = PowerFunction(Tilt_B, self.formula_modifier)
            Tilt_LR_Power 
            Tilt_FB_Power = 0

            exResult = np.array((StrafePower, DrivePower, UpdownPower, Tilt_FB_Power, Tilt_LR_Power, YawPower))
            exResult = exResult.reshape(6,1)

            FL = thrusterPreset(FLposition, FLthrust)
            FR = thrusterPreset(FRposition, FRthrust)
            BL = thrusterPreset(BLposition, BLthrust)
            BR = thrusterPreset(BRposition, BRthrust)
            TL = thrusterPreset(TLposition, TLthrust)
            TR = thrusterPreset(TRposition, TRthrust)

            thruster = [FL, FR, BL, BR, TL, TR]

            T = np.concatenate((thruster), axis=1)

            Tinv = np.linalg.pinv(T)
            finalList = Tinv.dot(exResult)

    def profileListener(self, profile):
        self.profile_change = profile #A, B, C, D
