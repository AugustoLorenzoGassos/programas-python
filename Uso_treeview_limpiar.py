# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:16:14 2026

@author: Augusto Lorenzo Gassós

"""
#Librerias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Datos
NM = []
ED = []
CI = []

with open("base.txt", "r") as BS:
    fila = BS.readlines()
    for filas in fila[1:]:
        filas = filas.strip()
        if filas == "":
            continue
        dato = filas.split(";")
        NM.append(dato[0])
        ED.append(dato[1])
        CI.append(dato[2])
        
def actulizar():
    with open("Base.txt", "w") as BS:
        print("Nombre;Edad;Ciudad", file=BS)
        for filas in tabla.get_children():
            dato = tabla.item(filas)["values"]
            print(dato[0],dato[1],dato[2], sep=";", file=BS)
def limpiar():
    for widget in frame_tree.winfo_children():
        widget.destroy()
    
def Opcion1():
    
    global tabla
    
    limpiar()
    
    #Aquí activara el tree/tabla
    tabla = ttk.Treeview(frame_tree, columns=("C1","C2","C3"), show="headings")
    tabla.heading("C1", text="Estado")
    tabla.heading("C2", text="Edad")
    tabla.heading("C3", text="Ciudad")
    
    for a,i in enumerate(NM):
        tabla.insert("","end",values=(i,ED[a],CI[a]))
    
    tabla.pack()
    
def Opcion2():
    limpiar()
    
def Eliminar():
    seleccion = tabla.selection()
    if seleccion:
        print("Eliminando elemento...")
        tabla.delete(seleccion)
        actulizar()
    else:
        messagebox.showerror("Error","No se ha seleccinado un elemento")

def añadir():
    
    def guardar():
        Nombre = EnNo.get()
        Edad = CoEd.get()
        Ciudad = EnCi.get()
        
        if Nombre == "" or Edad=="" or Ciudad=="":
            messagebox.showerror("Error","Campos vacios")
        else:
            with open("base.txt","a") as BS:
                print(f"{Nombre},{Edad},{Ciudad}\n", file=BS)
            NM.append(Nombre)
            ED.append(Edad)
            CI.append(Ciudad)
    
    limpiar()
    etiqueta_nombre = tk.Label(frame_tree, text="Nombre")
    etiqueta_edad = tk.Label(frame_tree, text="edad")
    etiqueta_ciudad = tk.Label(frame_tree, text="Ciudad")
    
    EnNo = tk.Entry(frame_tree)
    CoEd = ttk.Combobox(frame_tree, values=[18,19,20,21,22,23,24,25,26,27])
    EnCi = tk.Entry(frame_tree)
    
    etiqueta_nombre.grid(column=0, row=0)
    EnNo.grid(column=0, row=1)
    
    etiqueta_edad.grid(column=1, row=0)
    CoEd.grid(column=1, row=1)

    etiqueta_ciudad.grid(column=2, row=0)
    EnCi.grid(column=2, row=1)
    
    boton_guarda = tk.Button(frame_tree, text="Guardar")
    boton_guarda.grid(column=1, row=4, pady=20)

def evento_seleccion(event):
    print("")

def Cerrar_sesion():
    limpiar()
    actulizar()
    Ventana.destroy()

Ventana = tk.Tk()
Ventana.title = "Actualización de datos"
Ventana.geometry("600x400")
Ventana.resizable(False,False)

frame_control = tk.Frame(Ventana)
frame_tree = tk.Frame(Ventana)

lista = ttk.Combobox(frame_control, values=("Opcoin1","Opccion2"))

boton_eliminar = tk.Button(frame_control, text="Elininar elemento")
boton_añadir = tk.Button(frame_control, text="añadir elemento", command=añadir)
boton_cerrar = tk.Button(frame_control, text="Salir de la sesión", command=Cerrar_sesion)

lista.grid(column=0, row=0)
boton_añadir.grid(column=1, row=0)
boton_eliminar.grid(column=2, row=0)
boton_cerrar.grid(column=3, row=0)

#lista.bind("<<ComboboxSelected>>", evento_seleccion())

frame_control.pack(pady=20)
frame_tree.pack()

Opcion1()

Ventana.mainloop()

