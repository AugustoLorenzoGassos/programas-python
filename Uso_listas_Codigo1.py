# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:07:15 2026

@author: Augusto Lorenzo Gassós

"""

#import IPython.display as display
#from PIL import Image

#ImagenOK = Image.open("C:\Diplomado Python\OK.Jpg")
#ImagenErr = Image.open("C:\Diplomado Python\ERROR.Jpg")

NombreProducto = ""
Precio = 0.0
Cantidad = 0

Contador = 0
Productos = []

Opcion = ""
TotalInventario = 0
CantidadInventario = 0

while True:
    NombreProducto = input("Nombre del producto (escribir 'SALIR' para abandonar el registro'): ")
    if NombreProducto.upper() == "SALIR":
        break
    else:
        Precio = float(input("Precio: "))
        Cantidad = int(input("Cantidad: "))
    
        if Cantidad > 0:
            print("Producto disponible ")
            #display.display(Image.open("C:\Diplomado Python\OK.Jpg"))
        else:
            print("Producto agoitado")
            #display.display(Image.open("C:\Diplomado Python\ERROR.Jpg"))
        Productos.append([NombreProducto,Precio,Cantidad])

if len(Productos)>0:
    print("\n")
    print(f"{'Producto':<30}{'Precio':^10}{'Cantidad':^30}")
    while Contador < len(Productos):
        print(f"{Productos[Contador][0]:<30}{Productos[Contador][1]:>.2f}{Productos[Contador][2]:>30}")
        TotalInventario = TotalInventario + (float(Productos[Contador][1])*int(Productos[Contador][2]))
        CantidadInventario = CantidadInventario + int(Productos[Contador][2])
        Contador += 1
   
    print("\nCosto total del inventario:")
    print(TotalInventario)

match CantidadInventario:
    case Total if CantidadInventario < 1000:
        print("Inventario bajo")
    case Total if CantidadInventario >= 1000 and CantidadInventario <= 5000:
        print("Inventario medio")
    case _:
        print("Inventario alto")

