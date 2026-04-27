# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 16:29:34 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

VentanaPrincipal = Tk.Tk()

VentanaPrincipal.title("Inicio del sistema")
VentanaPrincipal.geometry("300x300")

LblSistema = Tk.Label(VentanaPrincipal, text="Sistema de gestión de restaurant")

LblUsuario = Tk.Label(VentanaPrincipal, text="Usuario: ")
LblContraseña = Tk.Label(VentanaPrincipal, text="Contraseña: ")

DatoUsuario = Tk.Entry(VentanaPrincipal)
DatoContraseña = Tk.Entry(VentanaPrincipal)

BtnAceptar = Tk.Button(VentanaPrincipal, text = "Aceptar")

LblSistema.grid(row=0, column=0)

LblUsuario.grid(row = 2, column=0)
DatoUsuario.grid(row=2, column=1)

LblContraseña.grid(row=3, column=0)
DatoContraseña.grid(row=3, column=1)

BtnAceptar.grid(row=4, column=1)

VentanaPrincipal.mainloop()
