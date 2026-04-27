# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:25:03 2026

@author: Augusto Lorenzo Gassós

"""

#Estructura del código
#Librerias
#Datos
#Clases para la creación de objetos
#Funciones definidas
#Código base (Proceso)
#Salidas


#Gestor de restaurant

#El programa constara de una interfaz de inicio de sesion simple
#Ingertaz de meseros con la información de la mesa (Disponibles y  no disponibles)
#Menu de comidada, bebidas, postres

#El mesero iniciaroa sesión y le mostrara las mesas disponibles y no disponibles
#Despues de seleccionaar la mesa, le apareceran las opciones
#1. si la mesa esta ocupada: 1) integrar otro alimento, 2)Pedir la cuenta
#2. Si la mesa esta disponible, 1)Encargar, 2)Reservar
#3. Ver pedidos

#MESA DISPONIBLE
#Encargar 1)Mostrar los menus y el usuario seleccionara que se qjuiere consumir
#Reservar 2) Solicitar el día y la hora de reservación. No menor de 3 días

Meseros = [["Augusto","1234","Augusto Lorenzo Gassós"],["JuanManuel","5678","Juan Manuel orenzo Gassós"],["Monica","Grem","Mónica Lorenzo Gassós"]]
Mesas = [["Mesa1","libre"],["Mesa2","libre"],["Mesa3","Ocupada"]]
Alimentos = [["Huevos rancheros",85],["Chilaquils rojos",80],["Chilaquiles verdes",80],["Enfrijoladas",75]]
Bebidas = [["Agua natural", 15],["Refrescos 600 ml",25],["Aguas de sabor",25],["Café",30]]
Postres = [["Gelatina",15],["Arroz con leche",25],["Flan",25]]

NombreMesero = ""
ContraseñaMesero = ""

Opcion = 0
Contador = 0
FinJornada = False

while True:
    
    print("1. Inicio de sesion")
    print("2. Salir")
    Opcion = int(input("Escribre el n úmero de opción: "))
    if Opcion == 3:
        break
    else:
        match Opcion:
            case 1:
                Contador = 0
                Encontrado = False
                NombreMesero = input("Ingresa tu usuario: ")
                ContraseñaMesero = input("Contraseña: ")
                while Contador < len(Meseros) and Encontrado == False:
                    if NombreMesero == Meseros[Contador][0] and ContraseñaMesero == Meseros[Contador][1]:
                        Encontrado = True
                    else:
                        Encontrado = False
                        Contador += 1
                print(Encontrado)
            case 2:
                break
    
    if Encontrado == True:
        print("Nombre del mesero: ",Meseros[Contador][2])
        while FinJornada == False:
            print("Selecciona la mesa que este libre (Para finalizar la jornada teclea 0 en la mesa): ")
            print(f"{'Mesa':^40}{'Status':^40}")
            for i in range(0,len(Mesas),1):
                print(f"{Mesas[i][0]:^40}{Mesas[i][1]:^40}")
            NumeroMesa = int(input("Escibe el número de mesa: "))
            print(NumeroMesa)
            if NumeroMesa == 0:
                FinJornada = True
            else:
                if Mesas[NumeroMesa-1][1] == "Ocupada":
                    print("1. Añadir alimentos\n2. Cerrar mesa")
                else:
                    print("1. Encargar\n2. Reservar")
                input("...")

"""
^40
                for a,i in enumerate(Meseros):
                    print(i)
                    if NombreMesero == i:
                        print("Encontrado")
                        Encontrado = True
                        if ContraseñaMesero == Meseros[a,1]:
                            print("Contraseña OK")
                        else:
                            print("Contraseña incorrecta")
                    else:                        
                        print("No encongtrado")                            

    print("Inicio de sesion".center(100))
    print("Esxcibir CERRAR en el nombre de usuario para cerrar sesión.")
    NombreMesero = input("Ingresa tu nombre de usuario: ")
    if NombreMesero.upper
    ContraseñaMesero = input("Contraseña: ")
    if NombreMesero.len() == 0 or ContraseñaMesero.len() == 0:
        print("El nombre de usaurio y/o contraseña no pueden estar vacios")
    else:
        if NombreMesero.upper() == "CEREAR":
            break
        else:
            while Contador <= len(Meseros):
                if NombreMesero == Meseros[Contador][0] and ContraseñaMesero == Meseros[Contador][1]:
                    print(f"Mesero {Meseros[Contador][2]}")
                else:
                    print("Credenciales invalidas")
                    break
                

    
"""