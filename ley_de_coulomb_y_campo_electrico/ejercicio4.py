from funciones import fuerza_componente_cero
import numpy as np

"""Las cargas puntuales Q1 y Q2 se localizan en (4, 0, −3) y (2, 0, 1), respectivamente. Si Q2 = 4 nC, halle Q1 de manera que:
a) −→E en (5, 0, 6) carezca de componente z.
b) La fuerza sobre una carga de prueba en (5, 0, 6) carezca de componente x."""
def main():
    carga_conocida = 4e-9
    punto_c_conocida = np.array([2,0,1])
    punto_c_no_conocida = np.array([4,0,-3])
    punto_carga_afectada = np.array([5,0,6])
    componente_cero = 0
    carga_no_conocida = fuerza_componente_cero(
        carga_conocida, 
        punto_c_conocida,
        punto_c_no_conocida,
        punto_carga_afectada,
        componente_cero
    )
    print(carga_no_conocida)

if __name__ == "__main__":
    main()