# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 17:10:26 2026

@author: Augusto Lorenzo Gassós

"""

#Ventana de registro

import tkinter as TK

VentanaRegistro = TK.Tk()
VentanaRegistro.title("Registro de usuario")
VentanaRegistro.geometry("700x500")

LblInicio = TK.Label(VentanaRegistro, text="Bienvenido")
LblSistema = TK.Label(VentanaRegistro, text="Llena todos los datos para completar tu registro")
LblInicio.pack()
LblSistema.pack()

FrameRegistro = TK.Frame(VentanaRegistro, width=700, height=300)
FrameRegistro.pack()

LblNombreUsuario = TK.Label(FrameRegistro, text = "Nombre")
LblSegundoNombreUsuario = TK.Label(FrameRegistro, text = "Segundo nombre")
LblPrimerApellido = TK.Label(FrameRegistro, text = "Primer apellido")
LblSegundoApellido = TK.Label(FrameRegistro, text = "Segundo apellido")

NombreUsuario = TK.Entry(FrameRegistro)
SegundoNombreUsuario = TK.Entry(FrameRegistro)
PrimerApellidoUsuario = TK.Entry(FrameRegistro)
SegundoApellidoUsuario = TK.Entry(FrameRegistro)

NombreUsuario.grid(row = 0, column= 0)
SegundoNombreUsuario.grid(row = 0, column = 1)
PrimerApellidoUsuario.grid(row = 0, column = 2)
SegundoApellidoUsuario.grid(row = 0, column = 3)

LblNombreUsuario.grid(row = 1, column = 0)
LblSegundoNombreUsuario.grid(row = 1, column = 1)
LblPrimerApellido.grid(row = 1, column = 2)
LblSegundoApellido.grid(row = 1, column = 3)

VentanaRegistro.mainloop()