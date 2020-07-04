import numpy as np
import math

#constants
sin = math.sin(45)
CG = np.array((0, 0, 0))
horizontalDist = [1,1,0] # FR x,y,z
verticalDist = [0,1,1] # TF x,y,z

FRpos = np.array((sin, sin, 0)) # position x,y,z
FRthr = np.array((sin, sin, 0)) # thrust direction
FRtor = FRthr.dot(FRpos)
print(FRtor)
#FR = np.array((sin, sin, 0, FRtor))




def thrusterPreset():
    pass
