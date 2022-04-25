import numpy as np

def main():
    #variables
    carga_puntual = 5e-9
    loc_cp = np.array([-3,4,0])
    y = 1
    z = 1
    carga_uniforme = 2e-9
    V = 110
    B = np.array([1,2,1])
    C = np.array([-2,4,1])

    #procedimiento
    ##no cambies nada si no sabes que p2
    constante = 9e9
    v_rb = B - loc_cp
    rb = np.sqrt(v_rb.dot(v_rb))
    v_rc = C - loc_cp
    rc = np.sqrt(v_rc.dot(v_rc))
    v_phiB = B - np.array([B[0],y,z])
    phiB = np.sqrt(v_phiB.dot(v_phiB))
    v_phiC = C - np.array([C[0],y,z])
    phiC = np.sqrt(v_phiC.dot(v_phiC))

    C = V - ((carga_puntual*constante) / rb)
    Vc = ((carga_puntual* constante)/rc) - 36*np.log(phiC) +C
    print(Vc)


if __name__ == "__main__":
    main()