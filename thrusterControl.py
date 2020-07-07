import numpy as np
import math

#constants
sin = math.sin(math.radians(45))
CG = np.array((0, 0, 0))
horizontalDist = [sin,sin,0] # FR x,y,z unit:m
verticalDist = [1,0,1] # TF x,y,z unit:m


def thrusterPreset(exResult):

    FRposition = np.array((horizontalDist[0], horizontalDist[1], horizontalDist[2])) # position x,y,z
    FRposition = np.subtract(FRposition, CG)
    FRthrust = np.array((-sin, sin, 0)) # thrust direction
    FRtorque = np.cross(FRposition, FRthrust) # torque = force x distance
    FR = np.concatenate((FRthrust, FRtorque)).reshape(6,1)

    FLposition = np.array((-horizontalDist[0], horizontalDist[1], horizontalDist[2]))
    FLposition = np.subtract(FLposition, CG)
    FLthrust = np.array((sin, sin, 0))
    FLtorque = np.cross(FLposition, FLthrust)
    FL = np.concatenate((FLthrust, FLtorque)).reshape(6,1)

    BLposition = np.array((-horizontalDist[0], -horizontalDist[1], horizontalDist[2]))
    BLposition = np.subtract(BLposition, CG)
    BLthrust = np.array((sin, -sin, 0))
    BLtorque = np.cross(BLposition, BLthrust)
    BL = np.concatenate((BLthrust, BLtorque)).reshape(6,1)

    BRposition = np.array((horizontalDist[0], -horizontalDist[1], horizontalDist[2]))
    BRposition = np.subtract(BRposition, CG)
    BRthrust = np.array((-sin, -sin, 0))
    BRtorque = np.cross(BRposition, BRthrust)
    BR = np.concatenate((BRthrust, BRtorque)).reshape(6,1)

    TLposition = np.array((verticalDist[0], verticalDist[1], verticalDist[2]))
    TLposition = np.subtract(TLposition, CG)
    TLthrust = np.array((0, 0, 1))
    TLtorque = np.cross(TLposition, TLthrust)
    TL = np.concatenate((TLthrust, TLtorque)).reshape(6,1)

    TRposition = np.array((-verticalDist[0], verticalDist[1], verticalDist[2]))
    TRposition = np.subtract(TRposition, CG)
    TRthrust = np.array((0, 0, 1))
    TRtorque = np.cross(TRposition, TRthrust)
    TR = np.concatenate((TRthrust, TRtorque)).reshape(6,1)

    thruster = [FL, FR, BL, BR, TL, TR]

    T = np.concatenate((thruster), axis=1)

    Tinv = np.linalg.pinv(T)
    output = Tinv.dot(exResult)
    return output

exResult = np.array((0,0,0,0,0,1)).reshape(6,1)
print(thrusterPreset(exResult))
