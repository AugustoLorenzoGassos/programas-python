# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 16:38:39 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

VentanaPrincipal = Tk.Tk()

VentanaPrincipal.title("Inicio del sistema")
VentanaPrincipal.geometry("300x300")

FramePrincipal = Tk.Frame(VentanaPrincipal, width=200, height=200)
FramePrincipal.pack()

#LblSistema = Tk.Label(VentanaPrincipal, text="Sistema de gestión de restaurant")

LblUsuario = Tk.Label(FramePrincipal, text="Usuario: ")
LblContraseña = Tk.Label(FramePrincipal, text="Contraseña: ")

DatoUsuario = Tk.Entry(FramePrincipal)
DatoContraseña = Tk.Entry(FramePrincipal)

LblUsuario.grid(row = 2, column=0)
DatoUsuario.grid(row=2, column=1)

LblContraseña.grid(row=3, column=0)
DatoContraseña.grid(row=3, column=1)

BtnAceptar = Tk.Button(VentanaPrincipal, text = "Aceptar")
BtnAceptar.pack()

VentanaPrincipal.mainloop()