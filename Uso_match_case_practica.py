# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 14:16:00 2026

@author: Augusto Lorenzo Gassós
"""

#Código 2
AutorizacionPiloto = True
CondicionesClima = True
PistaLibre = False

Despegar = (AutorizacionPiloto, CondicionesClima, PistaLibre)

match Despegar:
    case (0,0,0):
        print("Despegue denegado: revise las condiciones")
    case (0,0,1):
        print("Despegue denegado: revise las condiciones")
    case (0,1,0):
        print("Despegue denegado: revise las condiciones")
    case (0,1,1):
        print("Despegue denegado: revise las condiciones")
    case (1,0,0):
        print("Despegue denegado: revise las condiciones")
    case (1,0,1):
        print("Despegue denegado: revise las condiciones")
    case (1,1,0):
        print("Despegue denegado: revise las condiciones")
    case (1,1,1):
        print("Despegue autorizado: todas las condiciones necesarias se cumplen")