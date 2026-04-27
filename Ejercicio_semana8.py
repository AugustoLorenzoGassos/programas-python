# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:18:04 2026

@author: Augusto Lorenzo Gassós
"""

CapacidadTanque = 100
NivelActual = 0
Incremento = 10

with open("LLenado.txt", "w", encoding="utf-8") as f:
    while NivelActual < CapacidadTanque:
        NivelActual = NivelActual + Incremento
        print(f"El nivel actual de agua en e tanque es de: {NivelActual}")
        print(f"El nivel actual de agua en e tanque es de: {NivelActual}", file= f )
        if NivelActual >= 80 and NivelActual < CapacidadTanque:
            print(f"El nivel actual ({NivelActual} esta por alcanzar la capacidad total del tanque {CapacidadTanque})")
            print(f"El nivel actual ({NivelActual} esta por alcanzar la capacidad total del tanque {CapacidadTanque})", file = f)
    print("El tanque esta lleno a su máxima capacidad")
    print("El tanque esta lleno a su máxima capacidad", file = f)