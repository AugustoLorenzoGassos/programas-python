# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 18:20:24 2025
@author: Augusto Lorenzo Gassós

"""
NombreProducto = "Coca-Cola"
CantidadStock=15
Costo=16.5
Estado="Nuevo"
Area="A"
A=""

if CantidadStock <=0:
    print("Aerículo no disponible")
elif CantidadStock <= 5:
    print("Producto requiere reposición")
else:
    print("Producto dispiible")
    
if Estado=="Dañado":
    print("Mo puede venderse")
    print("Se marca para el retiro")
elif Estado=="Nuevo":
    print("Se permite venta con prioridad")
elif Estado=="Normal":
    print("Venta standar")
else:
    print("Estado no reconocido")
    
if Estado == "Dañado" and CantidadStock > 0:
    print("Advertencia")
    A = "Advertencia"
elif Estado=="Nuevo" and CantidadStock<5:
    print("Reposición urgente")
    A = "Reposición urgente"
elif Estado == "Normal" and CantidadStock>10:
    print("Venta  normal sin restricciones")
    A = "Venta  normal sin restricciones"
elif Estado == "Normal" and CantidadStock <5:
    print("Reposición")
    A = "Reposición"
else:
    print("Sin observaciones")
    A = "Sin observaciones"
    
ValorTotal = Costo * CantidadStock

Existe = True

if Existe:
    with open("c:/Diplomado Python/ReporteAlmacen.txt","a") as f:
        print(f"{'Nombre del producto':<20}{NombreProducto:<14}", file=f)
        print(f"{'Stock':<20}{CantidadStock:<15}", file=f)
        print(f"{'Estado':<20}{Estado:<15}", file=f)
        print(f"{'Estado':<20}{Estado:<15}", file=f)
        print(f"{'Resultado':<20}{A:<15}", file=f)
        print(f"{'Valor total':<20}{ValorTotal:<15}", file=f)
        print("="*45, file=f)
else:
    with open("c:/Diplomado Python/ReporteAlmacen.txt","w") as f:
        print(f"{'Nombre del producto':<20}{NombreProducto:<14}", file=f)
        print(f"{'Stock':<20}{CantidadStock:<15}", file=f)
        print(f"{'Estado':<20}{Estado:<15}", file=f)
        print(f"{'Estado':<20}{Estado:<15}", file=f)
        print(f"{'Resultado':<20}{A:<15}", file=f)
        print(f"{'Valor total':<20}{ValorTotal:<15}", file=f)
        print("="*45, file=f)
    



    