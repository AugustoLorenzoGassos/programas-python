# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:39:25 2026

@author: Augusto Lorenzxo Gassós
"""
import random

a = random.randint(-100, 100)
print(a)

while True:
    opciones = ["rojo","verde","azul","anarillo","naranja","morado"]
    seleccion = random.choice(opciones)
    print(f"El color seleccinado al azar fue {seleccion}")
    if seleccion == "rojo":
        break
    
random.shuffle(opciones)
print(opciones)

print(f"{random.random():.4f}")