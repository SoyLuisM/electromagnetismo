from sympy.abc import y,x
from sympy import integrate
import numpy as np

def main():
    punto_1 = np.array([0,3,0])
    punto_2 = np.array([1,3,0])
    punto_3 = np.array([1,-1,0])
    ec_1 = 3*x**2 + punto_1[1]
    ec_2 = punto_2[0]
    carga = -2e-6


    integral_1 = integrate(ec_1,(x,punto_1[0],punto_2[0]))
    integral_2 = integrate(ec_2, (y, punto_2[1],punto_3[1]))
    res = integral_1 + integral_2

    resultado = -1*(carga*res)
    print(integral_1)
    print(integral_2)
    print(resultado)

if __name__ == "__main__":
    main()