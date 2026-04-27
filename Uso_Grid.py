# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:15:38 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

VentanaPrincipal = Tk.Tk()
VentanaPrincipal.title("Ubicación con Grid")
VentanaPrincipal.geometry("300x300")

Etiqueta1 = Tk.Label(VentanaPrincipal, text="Etiqueta 1", bg="yellow")
Etiqueta1.grid(row=0, column=0)

Etiqueta2 = Tk.Label(VentanaPrincipal, text="Etiqueta 2", bg="red")
Etiqueta2.grid(row=1, column=0)

Boton1 = Tk.Button(VentanaPrincipal, text="Aceptar")
Boton1.grid(row=2, column=0)

EntradaDatos = Tk.Entry(VentanaPrincipal)
EntradaDatos.grid(row=3, column=0)

VentanaPrincipal.mainloop()

