# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:18:40 2026

@author: Augusto Lorenzo Gassós
"""

"""
ListaCompras = ["Pan","Leche","Huevos"]
ListaCompras.append(input("Ingresa un producto pra anadir a la lista: "))
print(ListaCompras)

ListaCompras[2]="Coca-cola"
ListaCompras.pop(1)

print(ListaCompras)
print(ListaCompras[2])
"""
Cona = []
Sina = []

while len(Cona)<3:
    dato = input("Ingresa un dato: ")
    if dato.lower().startswith("a"):
        Cona.append(dato)
    else:
        Sina.append(dato)
        
print("\nDatos que comienzan con a:")
print(Cona)
print("\nDatos que comienzan sin a:")
print(Sina)
