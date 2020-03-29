#Jessie Lazo CECS 229
import math
from plotting import plot

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT:
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * T - set consisting of points in S translated by z0
    """
    T = []
    for comp in S:
        temp = (comp + z0)
        T.append(temp)
    return set(T)
    pass



#T = translate(S, -1+2j)
#plot(S)


def scale(S, k):
    """
    scales the complex numbers of set S by k.
    INPUT:
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k

    """
    if k < 0:
        raise ValueError("ERROR: Scaling factor must be a positive float")
    T = []
    for comp in S:
        temp = (comp * float(k))
        T.append(temp)
    return set(T)
    pass


def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.
    INPUT:
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * T - set consisting of points in S rotated by theta radians

    """
    if(theta != 0):
        T = []
        c = complex(math.cos(theta), math.sin(theta)) #create c as a complex number for operator compatiblity
        for comp in S:
            temp = (comp * c)
            T.append(temp)
        return T
    else:
        return S
    pass

print(S)

#Problem 1
T = translate(S, 1+2j)
plot(T)

#Problem 2
T1 = scale(S, 2)
plot(T1)

#Problem 3
V = rotate(S, math.pi/12)
W = rotate(S, -math.pi/4)
plot(V)
plot(W)