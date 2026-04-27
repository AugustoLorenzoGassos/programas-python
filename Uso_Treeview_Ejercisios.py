# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:02:07 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as Tk
from tkinter import ttk
import os

def InsertarFila():
    Tabla.insert("", "end", values=(TextoNombre.get(), TextoEdad.get(), TextoPais.get(), TextoEstado.get(), TextoMunicipio.get()))
    ActualizarArchivo()
    
def EliminarFila():
    seleccionado = Tabla.selection()
    if seleccionado:
        Tabla.delete(seleccionado)
        print("Elemento eliminado")
    else:
        print("No se tiene seleccinado un elemento")
    ActualizarArchivo()
    
def MostrarFila():
    seleccinado = Tabla.selection()
    if seleccinado:
        #
        print("Datos seleccionados: ", seleccinado)

def ActualizarArchivo():
    with open(Base, "w") as Ac:
        print("Nombre;Edad;Pais;Estado;Municipio", file=Ac)
        for Filas in Tabla.get_children():
            DatoFila = Tabla.item(Filas)["values"]
            print(DatoFila[0],DatoFila[1],DatoFila[2],DatoFila[3],DatoFila[4], sep=";", file=Ac)

ListaNombre=[]
ListaEdad=[]
ListaPais=[]
ListaEstado = []
ListaMunicipio=[]

Base = "BASE1.Txt"
if not os.path.exists(Base):
    with open(Base, "w") as B:
        print("Nombre;Edad;Pais;Estado;Municipio", file=B)
else:
    print("Encontrado")
    with open(Base, "r") as B:
        fila = B.readlines()
        for i in fila[1:]:
            dato = i.strip().split(";")
            ListaNombre.append(dato[0])
            ListaEdad.append(dato[1])
            ListaPais.append(dato[2])
            ListaEstado.append(dato[3])
            ListaMunicipio.append(dato[4])

Ventana = Tk.Tk()
Ventana.geometry("1000x500")

FrameFormulario = Tk.Frame(Ventana)
FrameFormulario.pack()

EtiquetaNombre = Tk.Label(FrameFormulario, text = "Nombre: ")
EtiquetaEdad = Tk.Label(FrameFormulario, text = "Edad: ")
EtiquetaPais = Tk.Label(FrameFormulario, text = "País: ")
EtiquetaEstado = Tk.Label(FrameFormulario, text = "Estado: ")
EtiquetaMunicipio = Tk.Label(FrameFormulario, text = "Municipio: ")

TextoNombre = Tk.Entry(FrameFormulario)
TextoEdad = ttk.Combobox(FrameFormulario, values=[18,19,20,21,22,23,24,25,26,27,28,29,30])
TextoPais = Tk.Entry(FrameFormulario)
TextoEstado = Tk.Entry(FrameFormulario)
TextoMunicipio = Tk.Entry(FrameFormulario)

EtiquetaNombre.grid(column=0, row=0)
TextoNombre.grid(column=1, row=0)
EtiquetaEdad.grid(column=0, row=1)
TextoEdad.grid(column=1, row=1)
EtiquetaPais.grid(column=2, row=0)
TextoPais.grid(column=3, row=0)
EtiquetaEstado.grid(column=2, row=1)
TextoEstado.grid(column=3, row=1)
EtiquetaMunicipio.grid(column=4, row=0)
TextoMunicipio.grid(column=5, row=0)

BtnGuardar = Tk.Button(Ventana, text="Registrar", command=InsertarFila )
BtnGuardar.pack()

FrameTabla = Tk.Frame(Ventana)
FrameTabla.pack()

#Treeview
Tabla = ttk.Treeview(Ventana, columns=("C1","C2","C3","C4","C5"), show="headings")
Tabla.heading("C1", text="Nombre")
Tabla.heading("C2", text="Edad")
Tabla.heading("C3", text="Ciudad")
Tabla.heading("C4", text="Estado")
Tabla.heading("C5", text="Municipio")
Tabla.column("C1", width=200)
Tabla.column("C2", width=50)
Tabla.column("C3", width=150)
Tabla.column("C4", width=150)
Tabla.column("C5", width=150)
Tabla.pack()

for a,i in enumerate(ListaNombre):
    Tabla.insert("", "end", values=(i,ListaEdad[a],ListaPais[a],ListaEstado[a],ListaMunicipio[a]))

FrameBotones = Tk.Frame(Ventana)
FrameBotones.pack()

BtnEliminar = Tk.Button(FrameBotones, text="Eliminar", command=EliminarFila)
BtnEliminar.grid(column=0,row=0)
BtnMostrar = Tk.Button(FrameBotones, text="Mostrar", command=MostrarFila)
BtnMostrar.grid(column=1,row=0)

#BtnMostrar.pack()

Ventana.mainloop()

"""
Opcion = Tk.IntVar()
Opcion.set(0)

def Mostrar():
    print("Opcion elegida:", Opcion.get())
    match Opcion.get():
        case 1:
            print("Opcion 1")
        case 2:
            print("Opcion 2")
        case 3:
            print("Opción 3")
        case 4:
            print("Opcion 4")
        case 5:
            print("Opcion 5")

def AlSeleccionar(event):
    x = Combo.get()
    etiqueta.config(text=f"EL lenguaje seleccionado es: {x}")




#def Adquirir():
#    print(f"El lenguaje seleccinado es {Combo.get()}")


r1 = Tk.Radiobutton(Ventana, text="Opción 1", variable=Opcion, value=1, command=Mostrar)
r2 = Tk.Radiobutton(Ventana, text="Opción 2", variable=Opcion, value=2, command=Mostrar)
r3 = Tk.Radiobutton(Ventana, text="Opción 3", variable=Opcion, value=3, command=Mostrar)
r4 = Tk.Radiobutton(Ventana, text="Opción 4", variable=Opcion, value=4, command=Mostrar)
r5 = Tk.Radiobutton(Ventana, text="Opción 5", variable=Opcion, value=5, command=Mostrar)

r1.pack(anchor="w")
r2.pack(anchor="w")
r3.pack(anchor="w")
r4.pack(anchor="w")
r5.pack(anchor="w")

Tk.Label(Ventana, text="Elije un lenguaje de programación de la lista: ").pack(pady=10)
Lista = ["Python","Java","Java Script","C++","Rust"]
Combo = ttk.Combobox(Ventana, values=Lista)
Combo["state"]="readonly"
Combo.pack(pady=5)
#Combo.current(0)
Combo.bind("<<ComboboxSelected>>", AlSeleccionar)

etiqueta = Tk.Label(Ventana, text="Esperando a que se haga la elección ...").pack()

Tk.Button(Ventana, text="Guardar", command="Adquirir").pack()
"""

