# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 15:56:29 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk

Nombre = ["Usuario1","Usuario2","Usuaeio3"]
Edad = [21,34,26]
Ciudad = ["CDMX","Querétaro","Puebla"]

Ventana = Tk.Tk()
Ventana.geometry("200x200")

#VentanaPrincipal = Tk.Tk()
#VentanaPrincipal.geometry("1000x700")
#VentanaPrincipal.title("Ventana principal")


Estado = Tk.IntVar()

def MostrarEstado():
    print("Valor actual: ", Estado.get())

def Buscar():
    Encontrado = False
    UsuarioBuscar = Entrada1.get()
    for a,i in enumerate(Nombre):
        if i == UsuarioBuscar:
            Encontrado = True
            with open("Datos.txt", "w") as ficha:
                print(f"Usuario {UsuarioBuscar} tiene edad {Edad[a]} y vive en {Ciudad[a]}", file=ficha)
            break
    if Encontrado == True:
        print("Usuario encontrado")
    else:
        print("Usuario no registrado")

def AbrirVentanaPrincipal():
    VentanaPrincipal1 = Tk.Toplevel(Ventana)
    Ventana.iconify()
    
Check = Tk.Checkbutton(
    Ventana,
    text="Activar modo",
    variable=Estado,
    onvalue=1,
    offvalue=0,
    command=MostrarEstado,
    font=("Arial",12)
 )

Entrada1 = Tk.Entry(Ventana)
Entrada1.pack()

Boton1 = Tk.Button(Ventana, text="Aceptar", command=Buscar)
Boton1.pack()
BtnSalir = Tk.Button(Ventana, text="Salir", command=AbrirVentanaPrincipal)
BtnSalir.pack()

Check.pack(pady=20)

Ventana.mainloop()

