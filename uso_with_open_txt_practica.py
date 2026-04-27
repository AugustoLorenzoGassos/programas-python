# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 13:33:16 2026

@author: augus
"""

Humedad = 35
Llovido = False

with open("C:\Diplomado Python\Semana 6\ActividadesTareas\Riego.txt", "a", encoding="utf-8") as f:
    print(f"Humedad: {Humedad}llovido{Llovido}")
    if Humedad < 30 and Llovido == False:
        print("Resultado: Activar riego", file = f)
    elif Llovido == True:
        print("Resultado: No se necesita riego", file = f)
    elif Humedad > 30:
        print("Resultado: Humedad adecuada", file = f)

