# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 16:40:11 2026

@author: Augusto Lorenzo Gassós
"""

#Contador
Contador = 1
while Contador <= 5:
    print(f"El número es {Contador}")
    Contador += 1
print("Fin del bloque")

Contador = 1
while True:
    print(f"El número es {Contador}")
    if Contador >= 5:
        break
    else:
        Contador += 1
print("Fin del bloque")

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    print("El dobe es: ", numero * 2)

