# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 17:49:05 2026

@author: Augusto Lorenzo Gassós
"""

import random

Contador = 0
NumeroIgual = 0
NumeroAMayor = 0
NumeroBMayor = 0

while Contador < 10:
    NumeroA = random.randint(1,30)
    NumeroB = random.randint(1,30)
    if NumeroA > NumeroB:
        print(f"Número A {NumeroA} es mayor que número B {NumeroB}")
        NumeroAMayor += 1
    elif NumeroB > NumeroA:
        print(f"Número B {NumeroB} es mayor que número A {NumeroA}")
        NumeroBMayor += 1
    else:
        print(f"Los números son iguales: Número A: {NumeroA}, Número B {NumeroB}")
        NumeroIgual += 1
    Contador += 1
    
print("Numero A mayor: ", NumeroAMayor)
print("Numero B mayor: ", NumeroBMayor)
print("Numeros iguales: ", NumeroIgual)