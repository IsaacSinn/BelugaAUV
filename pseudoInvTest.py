import numpy as np
import math

sin = math.sin(45)

T = np.array((sin, sin, -sin, -sin, sin, -sin, sin, -sin, 1, -1, 1, -1))
T = T.reshape(3,4)
print(T)

Tinv = np.linalg.pinv(T)
print(Tinv)

R = np.array((1, 0, 0))
R = R.reshape(3,1)
print(R)

x = Tinv.dot(R)
print(x)
