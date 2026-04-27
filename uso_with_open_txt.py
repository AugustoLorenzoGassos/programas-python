# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 12:32:15 2026

@author: Augusto Lorenzo Gassós
"""

NombreUsuario1 = "Augusto Lorenzo Gassós"
EdadUsuario1 = 16

NombreUsuario2 = "Juan Manuel Lorenzo Gassós"
EdadUsuario2 = 17

with open("C:\Diplomado Python\Semana 5\ActividadesTareas\Salida.txt", "w", encoding="utf-8") as f:
    if EdadUsuario1 > 18 and EdadUsuario2 > 18:
        print("Ambos usuarios son mayores de edad", file = f)
    else:
        if EdadUsuario1 < 18 and EdadUsuario2 < 18:
            print("Ambos usuarios son menores de edad", file = f)
            print(f"{'Usuario':^40}{'Edad':^10}", file = f)
            print(f"{NombreUsuario1:^40}{EdadUsuario1:^10}", file = f)
            print(f"{NombreUsuario2:^40}{EdadUsuario2:^10}", file = f)
        else:
            if EdadUsuario1 < 18:
                print(f"Usuario {NombreUsuario1} es menor de edad", file = f) 
                print(f"{'Usuario':^40}{'Edad':^10}", file = f)
                print(f"{NombreUsuario1:^40}{EdadUsuario1:^10}", file = f)
            if EdadUsuario2 < 18:
                print(f"Usuario {NombreUsuario2} es menor de edad", file = f) 
                print(f"{'Usuario':^40}{'Edad':^10}", file = f)
                print(f"{NombreUsuario2:^40}{EdadUsuario2:^10}", file = f)
 