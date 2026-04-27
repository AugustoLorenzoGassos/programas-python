# -*- coding: utf-8 -*-
"""

@Author: Augusto Lorenzo Gassós
Editor de Spyder

Este es un archivo temporal.
"""

nombre = "Carlos"
parcial1 = 8.5
parcial2 = 9.0
proyecto = 9.3

#Cálculo de promedio
promedio = (parcial1+parcial2+proyecto) / 3

#1. IMpresión simple
print ("=== REPORTE DE CALIFICACIÓN ===")

#2 Impresión con comas (permite mezclar texyo y variables)
print("Alumno:", nombre)
print("Parcial 1:", parcial1, "Parcial 2:", parcial2, "Proyecto:",proyecto)

#3. Impresión con .format()
print("Promedio final (usando format) {:.2F}".format(promedio))

#4 Impresión con f-strings (la forma  modena mpas clara)
print(f"Alumno {nombre} obtuvo un promedio de {promedio:.2f} puntos.")

N1,E1,C1="Pedro",21,"Xalapa"
N2,E2,C2="María",32,"Orizada"
N3,E3,C3="Edgar",25,"Xalapa"
N4,E4,C4="Vanesa",18,"CDMX"

print(f"{'Nombre':<10}{'Edad':<10}{'Ciudad':<10}")
print(f"{N1:<10}{E1:<10}{C1:<10}")
print(f"{N2:<10}{E2:<10}{C2:<10}")
print(f"{N3:<10}{E3:<10}{C3:<10}")
print(f"{N4:<10}{E4:<10}{C4:<10}")
print("\n")

print(f"{'Nombre':<10}{'Edad':^5}{'Ciudad':>10}")
print(f"{N1:<10}{E1:^5}{C1:<10}")
print(f"{N2:<10}{E2:^5}{C2:<10}")
print(f"{N3:<10}{E3:^5}{C3:<10}")
print(f"{N4:<10}{E4:^5}{C4:<10}")

