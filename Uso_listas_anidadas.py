# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 16:12:36 2026

@author: Augusto Lorenzo Gassós
"""
#Listas paralelas

#Litas anidadas

"""""
DatosUsuario = [["Augusto Lorenzo",59,"Xalapa"],["Juan Manuel Lorenzo",57,"Xalapa"],["Mónica Lorenzo",61,"CDMX"],["Daniela Lorenzo",34,"Xalapa"],["Judith del Carmen Lorenzo",36,"Xalapa"]]
print(DatosUsuario[3][1])
"""""


C = 0
Consumo = 0

Platillos  = [["Tacos", 13],["Tortas",25],["Tamales",28],["Agua",18],["Refresco",25]]
while True:
    print(Platillos[C][0])
    C = C + 1
    if C >= len(Platillos):
        print("\nElije un platillo")
        OpcionPlatillo = input("Ingresa el nombre del platillo: ")
        C = 0
        while True:
            if Platillos[C][0] == OpcionPlatillo:
                Consumo = Consumo + Platillos[C][1]
                print("El costo del platillo es: ", Platillos[C][1])
                print("Consumo: ", Consumo)
                break
            else:
                C = C + 1
                if C >= len(Platillos):
                    print("Platillo no encontrado\n")
                    C = 0
                    break

