# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:11:11 2026

@author: Augusto Lorenzo Gassós

"""

import tkinter as tk

DISPONIBLES = []
OCUPADAS = []
RESERVADAS = []

with open("EJEMPLO1D.txt", "r") as BS1:
    Fila = BS1.readlines()

    for i1 in Fila:
        dato = i1.strip().split(";")
        DISPONIBLES.append(int(dato[0]))
        
with open("EJEMPLO2D.txt", "r") as BS2:
    Fila = BS2.readlines()

    for e in Fila:
        dato = e.strip().split(";")
        OCUPADAS.append(int(dato[0]))
 
def limpieza():
    for widget in Frame_Control.winfo_children():
        widget.destroy()


def ACTUALIZAR_BASES_TIMEPO_REAL():
    limpieza()
    Generar_botones()
    with open("EJEMPLO1D.txt", "w") as B1:
        for ii in DISPONIBLES:
            print(ii, file=B1)
            
    with open("EJEMPLO2D.txt","w") as B2:
        for aa in OCUPADAS:
            print(aa, file = B2)
 
    
def Boton_precionado(m):
    print(f"Se esta precionando el boton {m}")
    
    if m in DISPONIBLES:
        OCUPADAS.append(m)
        DISPONIBLES.remove(m)
        ACTUALIZAR_BASES_TIMEPO_REAL()
        
    elif m in OCUPADAS:
        DISPONIBLES.append(m)
        OCUPADAS.remove(m)
        ACTUALIZAR_BASES_TIMEPO_REAL()
        
def Generar_botones():
    TOTAL = len(DISPONIBLES) + len(OCUPADAS) + len(RESERVADAS)
    #EXTRAEMOS EL TOTAL DE BOTONES O MESAS DE LAS VARIABLES
    Columna = 0
    fila = 0
    for a in range(1,TOTAL+1,1):
        if a in DISPONIBLES:
            BT = tk.Button(Frame_Control, text = f"Mesa {a}",command = lambda m=a: Boton_precionado(m),bg="#27AE60")
        elif a in OCUPADAS:
            BT = tk.Button(Frame_Control, text = f"Mesa {a}",command = lambda m=a: Boton_precionado(m),bg="#FF0000")
        elif a in RESERVADAS:
            BT = tk.Button(Frame_Control, text = f"Mesa {a}",command = lambda m=a: Boton_precionado(m),bg="#FFFF00")
        
        BT.grid(column=Columna, row =fila )
        if Columna < 3:
            Columna = Columna + 1
        else:
            Columna = 0
            fila = fila + 1


Botones = tk.Tk()

Frame_Control = tk.Frame(Botones)
Frame_Control.pack()

Generar_botones()

Botones.mainloop()