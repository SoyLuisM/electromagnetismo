import numpy as np

"""
carga1 = carga que afecta a carga2 
carga2 = carga sobre la que se quiere calcular la fuerza
punto1 = punto en el espacio de carga1
punto2 = punto en el espacio de carga2
k = constante por defecto 9x10^-9
"""
def calcular_fuerza_carga(carga1, carga2, punto1, punto2,k = 9e9):
    #calculando vector entre carga1 y carga2
    R = punto2 - punto1

    #normalizando R1
    producto_R = np.sqrt(R.dot(R))

    aR = R/producto_R

    #calculando la fuerza en carga2 debido a carga1
    Fuerza = (k*(carga1*carga2)/producto_R**2)*aR

    return Fuerza

    
"""devuelve la carga necesaria para que la componente indicada sea cero"""
def fuerza_componente_cero(carga2, p_carga2,p_carga1,p_carga3,componente_cero):
    R1_3 = p_carga3 - p_carga1
    producto_R1_3 = np.sqrt(R1_3.dot(R1_3))
    R2_3 = p_carga3 - p_carga2
    producto_R2_3 = np.sqrt(R2_3.dot(R2_3))

    normal_R1_3 = R1_3/producto_R1_3
    normal_R2_3 = R2_3/producto_R2_3

    carga_no_conocida = (producto_R1_3**2 * carga2 * normal_R2_3[componente_cero]) / (normal_R1_3[componente_cero]*producto_R2_3**2)
    return carga_no_conocida