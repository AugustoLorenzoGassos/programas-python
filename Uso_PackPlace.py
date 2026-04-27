# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 15:59:11 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

VentanaPrincipal = Tk.Tk()

#Título
VentanaPrincipal.title("Mi primer proyecto")


#Tamaño
VentanaPrincipal.geometry("500x400")

EtiquetaPrincipal = Tk.Label(
    VentanaPrincipal, 
    text="Bienvenido a mi primera aplicación python")

EtiquetaSecundaria = Tk.Label(
    VentanaPrincipal, 
    text="Segundo texto")


EtiquetaPrincipal.pack()
EtiquetaSecundaria.place(x=0, y=200)



VentanaPrincipal.mainloop()
