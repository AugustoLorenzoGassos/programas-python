# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:01:04 2026

@author: Augusto Lorenzo Gassos
"""

import datetime

hoy = datetime.date.today()
ahora = datetime.datetime.now()

print(f"Hoy es {hoy}")
print(f"Fecha y hora exacta: {ahora}")

a = datetime.timedelta(days=7)
proyeccion = hoy + a
print(proyeccion)

HoyFormato = hoy.strftime("%A/%B/%Y %H:%M")
print(HoyFormato)

