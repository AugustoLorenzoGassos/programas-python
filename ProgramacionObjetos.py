# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:03:32 2026

@author: Augusto Lorenzo Gassós

"""

#Base que tenga 5 columnas. Muestra de 30
#========Productos
#nombre, costo, cantidad, area, descripción
#Harina 20 10,Granos,Harina ...

#Extraer cada producto, 
#encapsular en un objeto e 
#ingresarlos a una lista

#Accinamientos
#Generar una compra
#Rellenar producto

class Productos:
    def __init__(self, nombre, costo, cantidad, area, descripcion):
        self.nombre = nombre
        self.costo=costo
        self.cantidad=cantidad
        self.area=area
        self.descripcion = descripcion
        
    
    def generar_compra(self):
        nombre_producto = input("Ingresa el nombre del producto: ")
        encontrado=False
        for item_producto in lista_productos:
            if nombre_producto == item_producto.nombre:
                item_producto.cantidad = int(item_producto.cantidad)-1
                self.cantidad = item_producto.cantidad
                encontrado=True
                break
        if encontrado == True:
            print(f"La existencia actual del producto es {self.cantidad}") 
        else:
            print(f"El producto {nombre_producto} no fue encontrado")
    
    def rellenar_producto(self):
        nombre_producto = input("Ingresa el nombre del producto: ")
        encontrado=False
        for item_producto in lista_productos:
            if nombre_producto == item_producto.nombre:
                existencia_actual = int(input(f"Escribe la exisyencia alctial del producto {nombre_producto}: "))
                self.cantidad = existencia_actual
                encontrado = True
        if encontrado == True:
            print(f"La existencia actual del producto es {self.cantidad}") 
        else:
            print(f"El producto {nombre_producto} no fue encontrado")
            
lista_productos = []
lista_compras = []

with open("Productos.txt", "r") as Prod:
    Fila = Prod.readlines()
    for e in Fila[1:]:
        dato = e.strip().split(";")
        datos_producto = Productos(dato[0],dato[1],dato[2],[3],dato[4])
        lista_productos.append(datos_producto)   


while True:
    print("1. Generar compra\n2. Rellenar prooducto\n3.Salir")
    opcion = int(input("Escibe la opción: "))
    match opcion:
        case 1:
            for item_producto in lista_productos:
                print(f"{item_producto.nombre:<20}{item_producto.costo:^10}{item_producto.cantidad:^10}")
            item_producto.generar_compra()
        case 2:
            for item_producto in lista_productos:
                print(f"{item_producto.nombre:<20}{item_producto.costo:^10}{item_producto.cantidad:^10}")
            item_producto.rellenar_producto()
        case 3:
            break



