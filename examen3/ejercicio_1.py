import numpy as np

def main():
    #variables del ejercicio
    carga_1 = -4e-6
    carga_2 = 5e-6
    p_carga_1 = np.array([2,-1,3])
    p_carga_2 = np.array([0,4,-2])
    potencial_en = np.array([-1,-1,2])

    #procedimiento
    ##no cambies nada si no sabes que p2
    r1_rx = potencial_en - p_carga_1
    r2_rx = potencial_en - p_carga_2
    magnitud_v1 = np.sqrt(r1_rx.dot(r1_rx))
    magnitud_v2 = np.sqrt(r2_rx.dot(r2_rx))
    constante = 9e9
    resultado = ((constante*carga_1)/magnitud_v1) + ((constante*carga_2)/magnitud_v2)
    print(f"el resultado es {resultado}")

if __name__ == "__main__":
    main()