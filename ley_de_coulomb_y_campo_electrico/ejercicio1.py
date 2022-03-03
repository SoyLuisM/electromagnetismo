import numpy as np
"""Cargas puntuales de 1 mC y −2 mC se localizan en (3, 2, −1) y
(−1, −1, 4), respectivamente. Calcule 1a fuerza el´ectrica sobre una carga
de 10 nC localizada en (0, 3, 1) y la intensidad de campo el´ectrico en ese
punto. """

#Variables
q1 = 1e-3
q2 = -2e-3
q3 = 10e-9
p1 = np.array([3,2,-1])
p2 = np.array([-1,-1,4])
p3 = np.array([0,3,1])
k = 9e9
 

###########No modificar a partir de aqui amenos que sepas lo que haces XD
#calculo de R1 y R2
R1 = p3 - p1
R2 = p3 - p2

#normalizando R1 y R2
puntoR1 = np.sqrt(R1.dot(R1))
puntoR2 = np.sqrt(R2.dot(R2))

aR1 = R1/puntoR1
aR2 = R2/puntoR2

#calculando la fuerza en q3 debido a q1
F1 = (k*(q1*q3)/puntoR1**2)*aR1
#calculando la fuerza en q3 debido a q2
F2 = (k*(q2*q3)/puntoR2**2)*aR2

#calculando fuerza total
Ft = F1+F2

#calculando campo electrico
E = Ft/q3
##imprimiendo Resultados
print(f"La fuerza electrica en q3 debido a q1: {F1}")
print(f"La fuerza electrica en q3 debido a q2: {F2}")

print(f"La fuerza electrica sobre q3 debido a q1 y q2 es: {Ft}")

print(f"""el campo electrico debido a esta fuerza es:
{np.format_float_scientific(E[0], precision = 4, exp_digits=2)} Ax
{np.format_float_scientific(E[1], precision = 4, exp_digits=2)} Ay
{np.format_float_scientific(E[0], precision = 4, exp_digits=2)} Az
""")