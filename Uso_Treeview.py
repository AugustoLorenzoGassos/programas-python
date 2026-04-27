#-*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:06:26 2026

@author: Augusto Lorenzo Gassós

"""

import os

#Crea la carpeta principal
#Ruta = os.path.join("//Diplomado Python", CarpetaPrincipal)
CarpetaPrincipal = "ControlRST"
if not os.path.exists(CarpetaPrincipal):
    os.mkdir(CarpetaPrincipal)

#Crea la carpeta de meseros    
CarpetaMeserosRuta = os.path.join(CarpetaPrincipal, "MeserosBase")
if not os.path.exists(CarpetaMeserosRuta):
    os.mkdir(CarpetaMeserosRuta)
 
#Crea la carpeta de pedidos
CarpetaPedidosRuta = os.path.join(CarpetaPrincipal, "PedidosBase")
if not os.path.exists(CarpetaPedidosRuta):
    os.mkdir(CarpetaPedidosRuta)

#Crea el archivo de mesas disponibles
AR_DIS = os.path.join(CarpetaPrincipal, "Disponibles.txt")
if not os.path.exists(AR_DIS):
    with open(AR_DIS, "w") as Disp:
        print("Num_Mesa", file=Disp)

#Crea el arcghivo de mesas ocupada
AR_OCU = os.path.join(CarpetaPrincipal, "Ocupados.txt")
if not os.path.exists(AR_OCU):
    with open(AR_OCU, "w") as Ocup:
        print("Num_Mesa;Num_Pedido;Fecha;HoraMesero", file=Ocup)

#Crea el archivo de mesas reservadas
AR_RES = os.path.join(CarpetaPrincipal, "Reservados.txt")
if not os.path.exists(AR_RES):
    with open(AR_RES, "w") as Rese:
        print("Num_Mesa;Num_Pedido;Fecha;Mesero", file=Rese)

#Crea el archivo de meseros
ArchivoMeserosBase = os.path.join(CarpetaMeserosRuta, "MeserosBase.txt")
if  not os.path.exists(ArchivoMeserosBase):
    with open(ArchivoMeserosBase, "w") as Meseros:
        print("ID;NOMBRE;APELLIDO", file=Meseros)

#Crea el archivo de pedidos
ArchivoPedidosBase = os.path.join(CarpetaPedidosRuta, "PedidosBase.txt")
if  not os.path.exists(ArchivoPedidosBase):
    with open(ArchivoPedidosBase, "w") as Pedidos:
        print("NumPedido;NumMesa;CantidadProductos;IDMeasero;Fecha;Hora;Pagado", file=Pedidos)

Mesas_disponibles = []
Mesas_ocupadas = []
Mesas_Reserva = []
ID_Mesero = []
Contraseña_Mesero = []

#Extraer información de mesas disponibles
with open(AR_DIS, "r") as Disp:
    Linea = Disp.readlines()
    for l in Linea[1:]:
        Datos = l.strip().split(";")
        Mesas_disponibles.append(Datos[0])

#Extraer información de mesas ocupadas
with open(AR_DIS, "r") as Ocup:
    Linea = Ocup.readlines()
    for l in Linea[1:]:
        Datos = l.strip().split(";")
        Mesas_ocupadas.append(Datos[0])

#Extraer información de mesas reservadas
with open(AR_RES, "r") as Reserv:
    Linea = Reserv.readlines()
    for l in Linea[1:]:
        Datos = l.strip().split(";")
        Mesas_Reserva.append(Datos[0])
        
with open(ArchivoMeserosBase, "r") as Meseros:
    Linea = Meseros.readlines()
    for l in Linea[1:]:
        Datos = l.strip().split(";")
        ID_Mesero.append(Datos[0])
        Contraseña_Mesero.append(Datos[1])

print("Meseros")

        
