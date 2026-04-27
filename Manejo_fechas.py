# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 18:24:07 2026

@author: augus
"""

import datetime
from datetime import timedelta

fecha = datetime.datetime.today()
FechaFormato = fecha.strftime("%d/%m/%Y")
FechaMaxima = fecha + timedelta(days=3)

FechaComparar = input("Ingresa una fecha: ")
FechaComparar = datetime.datetime.strptime(FechaComparar, "%d/%m/%Y")

#FechaMaxima = FechaFormato - datetime.timedelta(days=3)
#print(FechaMaxima)

if FechaComparar <= FechaMaxima:
    print("Fecha invalida")
else:
    print("Fecha valida")
    
