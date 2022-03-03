import numpy as np
from funciones import calcular_fuerza_carga

def main():
    #Variables
    q1 = 5e-6
    q2 = -4e-6
    p1 = np.array([3,2,1])
    p2 = np.array([-4,0,6])

    fuerza_en_q1 = calcular_fuerza_carga(carga1 = q2, carga2 = q1, punto1 = p2, punto2 = p1)

    print(fuerza_en_q1)

if __name__ == "__main__":
    main()