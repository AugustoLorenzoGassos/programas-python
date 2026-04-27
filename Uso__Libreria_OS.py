# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 17:09:21 2026

@author: Augusto Lorenzo Gassós
"""

import os

print("Achivpos en Diploado python")
Archivos1 = os.listdir("c:\\")
print(Archivos1)

Archivos = os.listdir('.')
print("Archivos en la carpeta actual:", Archivos)

if not os.path.exists("NuevaCarpeta"):
    os.mkdir("NuevaCarpeta")

print("\nDirectorio actual")
print(os.getcwd())

print("\nContenido del directorio actual")
print(os.listdir('.'))

print("\nCrear una carpeta MiCarpeta")
if not os.path.exists("MiCarpeta"):
    os.mkdir("MiCarpeta")
    
print("\nCrerar carpetas anidadas")
RutaAnidada = os.path.join("MiCarpeta", "sub1", "sub2")
if not os.path.exists(RutaAnidada):
    os.makedirs(RutaAnidada)
    
