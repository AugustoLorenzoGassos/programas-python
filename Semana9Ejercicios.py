# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:53:35 2026

@author: Augusto Lorenzo Gassos
"""

Numero1 = input("Ingresa un número: ")
Numero2 = input("Ingresa un segundo número: ")
Numero2 = int(Numero2)

if Numero1.isdigit():
    Numero1 = int(Numero1)
else:
    print("No es un número")

Suma = Numero1 / Numero2
print(Suma)


