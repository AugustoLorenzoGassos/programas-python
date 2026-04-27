# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 13:04:20 2025

@author: Augusto Lorenzo Gassós
Ejercic 5 Semana 4
"""

Nombre = "Ana"
Edad = 23
Promedio = 9.3571

Nombre1 = "Augusto"
Edad1 = 59
Promedio1 = 9.7569

Nombre2 = "Juan"
Edad2 = 57
Promedio2 = 9.1224

Nombre3 = "Mónica"
Edad3 = 61
Promedio3 = 10.0000

print(f"Nombre: {Nombre}, Edad: {Edad}, Promedio: {Promedio}")

print(f"{'Nombre:':<10}{'Edad:':<10}{'Promedio:':^10}")
print(f"{Nombre:<10}{Edad:<10}{Promedio:^10.2f}")
print(f"{Nombre1:<10}{Edad1:<10}{Promedio1:^10.2f}")
print(f"{Nombre2:<10}{Edad2:<10}{Promedio2:^10.2f}")
print(f"{Nombre3:<10}{Edad3:<10}{Promedio3:^10.2f}")

with open("Salida.txt", "w", encoding="utf-8") as f:
    print(f"{'Nombre:':<10}{'Edad:':<10}{'Promedio:':^10}", file=f)
    print(f"{Nombre:<10}{Edad:<10}{Promedio:^10.2f}", file=f)


with open("Salida.txt", "a", encoding="utf-8") as f:
    print(f"{Nombre1:<10}{Edad1:<10}{Promedio1:^10.2f}", file=f)
    print(f"{Nombre2:<10}{Edad2:<10}{Promedio2:^10.2f}", file=f)
    print(f"{Nombre3:<10}{Edad3:<10}{Promedio3:^10.2f}", file=f)
