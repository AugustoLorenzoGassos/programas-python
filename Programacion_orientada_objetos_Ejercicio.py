# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:55:46 2026

@author: Augusto Lorenzo Gassós

"""

import os

#Sistema de gestión de inventario
#Registrar productos
#Comprar productos
#Búsqueda de producto
#Filtrar productos
#Salir

#Definición de la clase y métpdps
#Atributos IdArticulo, nombre, costro, cantidad, área
#Método: Ver información, Actualizar datos, generar reporte por prodcuto, costo totakl de inventario, compra
class Producto():
    
    def __init__(self, IdArticulo, nombre, costo, cantidad, area):
        self.IdArticulo = IdArticulo
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        self.area = area
       
    def ver_informacion(self):
        print("imprimir información")
        
    def generar_reporte():
        print("generar reporte")
    
    def actualizar_datos():
        print("actualizar datos")
    
    def costo_invebtario():
        print("costo del inventario")
        
    def comprar_producto():
        print("comprar producto")

#Declaración de funciones
def registrar_producto():
    print("\nRegistrar producto\n")
    VIdArticulo = input("Identificador del artículo: ")
    VNombre = input("Nombre del artículo: ")
    VCosto = float(input("Costo del producto: "))
    VCantidad = int(input("Cantidad del producto: "))
    VArea = input("Área de almacenaje: ")
    if len(VIdArticulo)>0 and len(VNombre)>0 and VCosto>0 and VCantidad>0 and len(VArea)>0:
        item_producto = Producto(VIdArticulo, VNombre, VCosto, VCantidad, VArea)
        lista_productos.append(item_producto)
        
def comprar_producto():
    print("Comprar producto")
    
def buscar_producto():
    print("\nBuscar producto\n")
    producto_buscar = input("Ingresa el id del producto: ")
    for item_producto in lista_productos:
        if item_producto.IdArticulo == producto_buscar:
            print(item_producto.nombre)
        else:
            print("\nProducto no encontrado")
    
def filtar_informacion():
    print("filtrar")
   
def listar_inventario():
    print("\nLista de artículos\n")
    for articulo in lista_productos:
        print(articulo.nombre)
    input("\nPresiona enter para continuar ...")

#Se van a almacenar los productos registrados (instancias de la clase productos)
lista_productos = []

#Código principal del sistema
while True:
    
    #Definición del menu
    print("Sistema de inventario".center(100))
    print("Opciones del sistema:\n")
    print("1. Registrar producto\n2. Comprar produrcto\n3. Buscar producto\n4. Filtrar\n5. Listar inventario\n6. Salir")
    
    #Lectura de la opción
    try:
        Opcion = int(input(("\nSelecciona la opcoón: ")))
    except ValueError:
        Opcion = 0
    
    #Validación de la opción seleccionada
    match Opcion:
        case 1:
            registrar_producto()
        case 2:
            comprar_producto()
        case 3:
            buscar_producto()
        case 4:
            filtar_informacion()
        case 5:
            listar_inventario()
        case 6:
            break
        case _:
            print("\nOpcion no reconocida")
            Continuar = input("¿Intentar nuevamente? (S/N) ")
            if Continuar.lower() == "s":
                os.system("cls")
                continue
            else:
                break
        