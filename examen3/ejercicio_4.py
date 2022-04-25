from numbers import Integral
import numpy as np
from sympy.abc import r
from math import sin,cos,pi,radians

def main():
    A = np.array([1,30,120])
    B = np.array([5,60,50])
    carga = 10e-6
    #paso 1
    r= A[0]
    theta = A[1]
    phi = A[2]
    integral_1 = (10/r**2)*sin(radians(theta))*cos(radians(phi))
    #paso 2
    r= B[0]
    theta_2 = B[1]
    phi_2 = B[2]
    integral_2 = (10/r**2)*sin(radians(theta_2))*cos(radians(phi_2))
    print(integral_1)
    print(integral_2)
    #paso 3
    W = carga*(integral_2-integral_1)
    print(W)
if __name__ == "__main__":
    main()