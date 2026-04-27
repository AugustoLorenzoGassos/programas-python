# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 16:07:12 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

VentanaPrincipal = Tk.Tk()

VentanaPrincipal.title("Inicio del sistema")
VentanaPrincipal.geometry("300x300")

#Etiqueta1 = Tk.Label(VentanaPrincipal, text="Sistema de gestión de restaurant")
#Etiqueta1.grid(row=0, column=0)

LblUsuario = Tk.Label(VentanaPrincipal, text="Usuario: ")
LblContraseña = Tk.Label(VentanaPrincipal, text="Contraseña: ")

DatoUsuario = Tk.Entry(VentanaPrincipal)
DatoContraseña = Tk.Entry(VentanaPrincipal)

BtnAceptar = Tk.Button(VentanaPrincipal, text = "Aceptar")

LblUsuario.pack()
DatoUsuario.pack()
LblContraseña.pack()
DatoContraseña.pack()
BtnAceptar.pack()

VentanaPrincipal.mainloop()



