# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:11:11 2026

@author: Augusto Lorenzo Gassós

"""

#Librerias

import tkinter as tk

#base de datos

#Clases y objetos

class persona:
    #Atributos o parámetros
    def __init__(self,nombre,edad,ciudad,idioma):
        self.nombre=nombre
        self.edad=edad
        self.ciudad=ciudad
        self.idioma=idioma
        self.escuela = "CETEC"
        self.calificacion = []
        
    #Accionamientos / métodos
    def cargar_calificacion(self):
        print("Función de calificación")
        while True:
            cal = input("Ingresa la calificación de los parciales: ")
            if cal.isdigit() and int(cal)>=0 and int(cal)<=100:
                self.calificacion.append(int(cal))
                print("calificación almacenada correctamente")
            else:
                print("Calificación no válida")
            if(len(self.calificacion))>=3:
                break
        print(self.calificacion)
        
    def informacion(self):
        print(f"Nombre: {self.nombre}\nEdad:{self.edad}\nCiudad: {self.ciudad}\nIdioma: {self.idioma}")
        if (len(self.calificacion)) == 3:
            Suma = 0
            for i in self.calificacion:
               Suma += i
            promedio = Suma/3
            print(f"Promedioo final: {promedio}")
        else:
            print("El promedio no se puedo calcular")

    def Ventana(self):
        Ventana = tk.Tk()
        tk.Label(Ventana, text=f"Nombre: {self.nombre}").pack()
        tk.Label(Ventana, text=f"Edad: {self.edad}").pack()
        Ventana.mainloop()
        
#Generación del objeto
alumno_01 = persona("Augusto", 59, "Xalapa", "Español")

#Funciones

#Código base
alumno_01.informacion()
alumno_01.Ventana()

#alumno_01.cargar_calificacion()
#alumno_01.informacion()

