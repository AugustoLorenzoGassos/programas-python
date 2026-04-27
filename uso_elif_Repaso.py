# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:23:26 2026

@author: Augusto Lorenzo Gassós
"""

# Menor a  cero = mucho frío
# de 0 a 10 = Frío
# de 10 a 20 = Fresco
# de 20 a 27 = Normal
# de 27 a 37 = Calor
# de 37 en adelante = Mucho calor

Temperatura = 45

if Temperatura < 0:
    print("Mucho frío")
else:
    if Temperatura < 10:
        print("Frío")
    else:
        if Temperatura < 20:
            print("Fresco")
        else:
            if Temperatura < 27:
                print("Normal")
            else:
                if Temperatura < 37:
                    print("Calor")
                else:
                    print("Mucho calor")

Temperatura = 15
if Temperatura < 0:
    print("Mucho frío")
elif Temperatura < 10:
    print("Frío")
elif Temperatura < 20:
    print("Fresco")
elif Temperatura < 27:
    print("Normal")
elif Temperatura < 37:
    print("Calor")
else:
    print("Mucho calor")
    