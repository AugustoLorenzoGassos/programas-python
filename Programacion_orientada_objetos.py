# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:59:43 2026

@author: Augusto Lorenzo Gassós

"""

#import tkinter

#Librerias
#Base de datos
#Clases
class personal:
    #Atriutos, metodos
    def __init__(self,IdPersonal, nombre, apellido, turno, salario, area, tipo_contrato, tiempo):
        self.IdPersonal = IdPersonal
        self.nombre = nombre
        self.apellido = apellido
        self.turno = turno
        self.salario = salario
        self.area = area
        self.tipo_contrato = tipo_contrato
        self.tiempo = tiempo
    
    def calcular_quincena(self):
        pago_total = self.salario * self.tiempo
        print(f"El pago quincenal es de {pago_total:.2f}")
        
    def cambio_horario(self):
        print("Acción de cambio")

#Objetos
#Funciones
#Código base

Empleado1 = personal(1234, "Augusto", "Lorenzo", "Matutino", 15000, "Sistemas", "Eventual", 8)
Empleado1.calcular_quincena()

Empleado2 = personal(5678, "Mónica", "Lorenzo", "Matutino", 10000, "Sistemas", "Eventual", 8)
Empleado2.calcular_quincena()

Empleado3 = personal(9012, "Juan Manual", "Lorenzo", "Matutino", 11000, "Sistemas", "Eventual", 8)
Empleado3.calcular_quincena()
