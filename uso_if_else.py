# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 12:51:40 2025

@author: Augusto Lorenzo Gassós
Tarea de semana 4: Repaso pasar pseudocódigo a python

"""

SalarioBase = 9000
Bono = 1000
Descuento = 500
HorasExtra = 5
PagoHoraExtra = 100
Activo = True
Fatlas = 1

SalarioTotal = SalarioBase + Bono + (HorasExtra * PagoHoraExtra) - Descuento
if SalarioTotal > 12000:
    print ("Salario alto")
else:
    if SalarioTotal >= 10000:
        print ("Salario medio")
    else:
        print("Salatio bajo")

if Activo == True and Fatlas <=2:
    print ("Empleado con buen desem peño")
else:
    print("Empleado con advertencia")
    
    