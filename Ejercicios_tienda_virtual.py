# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:01:23 2026

@author: Augusto Lorenzo Gassós
"""

#Genera un menu interactivo
#>Memu de compras

#1) Ver productos
#2) Comprar productos
#3) Salir

#El usuario debra salir del siste, si y sólo si, selecciona la opción 3
#1. Deberá mostrar tres productos con sdus precios y seleccionar sóño 1
#2. Preguntar cuantas pieas y  mostrar el total a pagar en un mensaje
#Mensaje con los datos de la compra comofecha y bora actual

import datetime

Opcion = 0
IdProducto = 0
DescProducto = ""
CostoProducto = 0
CantidadProducto = 0
TotalCompra = 0

while True:
    print("1. Ver productos")
    print("2. Comprar procutos")
    print("3. Salir")
    Opcion = int(input("Selecciona la opción del menú:"))
    match Opcion:
        case 1:
            print("1. Papel\n2.Libretas\n3.Gomas")
            IdProducto = int(input("Ingrese el producto a comprar"))
            match IdProducto:
                case 1:
                    DescProducto = "Papel"
                    CostoProducto = 14
                case 2:
                    DescProducto = "Libretas"
                    CostoProducto = 23
                case 3:
                    DescProducto = "Gomas"
                    CostoProducto = 15
                case _:
                    print("Producto no identificado")
                    
        case 2:
            print("Proceso de compra")
            CantidadProducto = int(input("¿Cuántas piezas de deseas comprar: "))
            TotalCompra = CantidadProducto * CostoProducto
            print(f"Producto {DescProducto} | Cantidad adquirida {CantidadProducto} | Costo del artículo {CostoProducto}")
            print(f"Total a pagar: {TotalCompra}"),
            print("Fecha y hora de la compra: ", datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
        case 3:
            break
        case _:
            print("Opción fuera del menú")
            
print(("\n"))
print("Gracias por acudir a nuestra tienda vistual")