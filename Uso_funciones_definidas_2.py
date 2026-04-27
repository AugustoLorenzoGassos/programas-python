# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 18:04:41 2026

@author: Augusto Lorenzo Gassós

"""

#Funciones definidas sin parámetro y sin retorno

def Operaciones():
    #Proceso
    numero1 = int(input("Primer número: "))
    numero2 = int(input("Seguindo número: "))
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    dividir = numero1 / numero2
    print(suma, resta, multiplicacion, dividir)
    
while True:
    print("")
    Selección = input("Seleccione una opción: ")
    match Selección:
        case "1":
            Operaciones()
        case "2":
            Operaciones()
        case "3":
            Operaciones()
        case "4":
            break
        case _:
            print("Opción fuera de rango")
            
    
            