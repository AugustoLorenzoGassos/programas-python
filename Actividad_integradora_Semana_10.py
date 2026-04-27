# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 20:13:36 2026

@author: Augusto Lorenzo Gassós

"""

import datetime
import random
import os

NivelMinimo = 0
NivelMaximo = 0
Continuar = ""

ActivarCalefaccion = 0
ActivarVentilador = 0

print("Sistema automático de control de temperatura".center((200)))
print("Fecha y hora de inicio de monitoreo: ",datetime.datetime.now().strftime("%d%m/%Y %H:%M"))
print("\n")

NivelMaximo = int(input("Defina el nivel máximo aceptable: "))
NivelMinimo = int(input("Defina el nivel mínimo aceptable: "))
Status = 0
TxtStatus = ""

with open("Registro.txt", "a", encoding="utf-8") as Registro:
    print(f"{'Fecha':<40}{'Temperatura':^30}{'Acción tomada':<40}", file=Registro)

    while True:
        TemperaturaAcual = random.randint(0, 50)
        if TemperaturaAcual < NivelMinimo:
            Status = 1
            TxtStatus = "Activar calefacción"
            ActivarCalefaccion += 1
        elif TemperaturaAcual > NivelMaximo:
            Status = 2
            ActivarVentilador += 1
            TxtStatus = "Activar ventiladores"
        else:
            Status = 3
            TxtStatus = "Sistema estable"
        print("\n")
        print("Temperatura actual: ", TemperaturaAcual)
        print("Estado: ", TxtStatus)
                
        print(f"{datetime.datetime.now().strftime("%d%m/%Y %H:%M"):<40}{TemperaturaAcual:^30}{TxtStatus:<40}", file = Registro)
        
        Continuar = input("¿Continuar con el monitoreo s/n?: ")
        if Continuar == "n":
                                        break
    print("\nSistema de monitoreo apagado")
    print("Fecha y hora de ciere de monitoreo: ",datetime.datetime.now().strftime("%d%m/%Y %H:%M"))
    print(f"Los ventiladores se accionaron {ActivarVentilador} veces")
    print(f"La calefacción se activó {ActivarCalefaccion} veces")

