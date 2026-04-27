# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 13:30:45 2026

@author: Augusto Lorenzo Gassós

"""

LitrosActual = 100

NombreCliente = ""
CantidadLitros = 0
CantidadClientes = 0
NUmeroLitros = 0

while True:
    NombreCliente,CantidadLitros = input("Escriba el nombre del cliente y la cantidad de litros separados por coma: ").split(",")
    if CantidadLitros.isdigit():
        CantidadLitros = int(CantidadLitros)
        if CantidadLitros <= LitrosActual:
            LitrosActual = LitrosActual - CantidadLitros
            CantidadClientes += 1
            if LitrosActual == 0:
                print("Bomba fuera de servicio")
                break
            elif LitrosActual > 50:
                print("Nivel alto")
            elif LitrosActual >= 20 and LitrosActual <= 50:
                print("Nivel medio")
            else:
                print("Nivel bajo")
        else:
           print("No hay suficiente gasolina") 
    else:
        print("Error en la cantidad de litros")
        
match CantidadClientes:
    case Cantidad if CantidadClientes > 10:
        print("Día muy activo")
    case Cantidad if CantidadClientes >= 5 and CantidadClientes <= 10:
        print("Día regular")
    case _:
        print("Día con poca actividad")