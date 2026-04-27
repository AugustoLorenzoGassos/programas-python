# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:47:48 2026

@author: Augusto Lorenzo Gassós

"""
#Librerias
#Base de datos
NombreUsuario = "alorenzo"
NumeroCuenta =  "5511281636"
ClaveUsuario = "1234"
ContraseñaUsuario = "5678"

#Clases
#Funciones definidas por el usuario

#Generar menú interactivo con input para cuenta de banco, debe de inlcuir las siguientes niveles:
#1 un menú principal al ejecutar el progranaque sea:
        #1) Inicial sesión
        #2) Registrarse
        #3) Cerrar sesión
        
#2. Si se ingresa la opción 2 deberá soliictar lo siguiente:
    #Usuario o número de cuenta
    #Contraseña

#3. Si se ingresa la opción 2 deberá solicitar lo siguiente:
    #Número de cuenta, Nombre complero, NIP (solicitar 2 veces) y contraseña (también solicitar dos veces)

#4. Si se ingresa la opción 3. Salir del programa

Opcion = ""

Usuario = ""
Contraseña = ""

NombreRegistro = ""
ApellidoRegistro = ""
UsuarioRegistro = ""
ContraseñaRegistro = ""
ContraseñaConfirmar = ""
NIPConfirmar = ""

Intentos = 0
StatusInicioSesion = False

while True:
    Opcion = input("Seleccione la opción de la suguiente lista:\n\n1.Inicial sesión\n2.Registrarse\n3.Cerrar sesión\n")
    match Opcion:
        case "1":
            while Intentos < 3 and StatusInicioSesion == False:
                Usuario = input("Escibre tu nombre de usuario o número de cuenta: ")
                Contraseña = input("Escribe tu contraseña: ")
                if (Usuario == NombreUsuario or Usuario ==  NumeroCuenta) and Contraseña == ContraseñaUsuario:
                    StatusInicioSesion = True
                else:
                    Intentos = Intentos + 1
            if StatusInicioSesion == True:
                print("\nInicio de sesión correcto")
                break
            else:
                print("\nUsaste tus tres intentos. Inicio de sesión fallido")
                break
        case "2":
            NombreRegistro, ApellidoRegistro = input("Ingresa tu nombre completo separados con ,").split(',')
            UsuarioRegistro = input( "Escibre tu nombre de usuario o número de cuenta: ")
            NumeroCuentaRegistro = input("Escribe tu número de cuneta: ")         
            CorreoRegistro = input("Escribre tu cuneta de correo para registro: ")
            CelularRegistro = input("Escribet tu numero de celular para registro: ")
            ContraseñaRegistro = input("Escribe tu contraseña: ")
            while ContraseñaRegistro != ContraseñaConfirmar:
                ContraseñaConfirmar = input("Confirma la contraseña: ")
                if ContraseñaRegistro != ContraseñaConfirmar:
                    print("Contraseña incorrecta")
            print("Contraseña correcta")
            NIPRegistro = input("Escribe tu NIP: ")
            while NIPRegistro != NIPConfirmar:
                NIPConfirmar = input("Confirma tu NIP: ")
                if NIPRegistro != NIPConfirmar:
                    print("NIP incorrecto")
            print("NIP correcto")
        case "3":
            break
        case _:
            print("Oción no registrada")

    