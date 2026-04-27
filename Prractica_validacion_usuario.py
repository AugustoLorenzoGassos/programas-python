# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:23:14 2026

@author: Augusto Lorenzo Gassós
"""

#Usuario
#Contraseña:
#Validar 
#3 oportuniades

Oportunidades = 1
UsuarioValido = False
IniciarSesion = False

Usuario = "alorenzo"
Contraseña = "dajuau051429"

while True:
    Opcion = input("Escribe la acción a realizar (Inicio para iniciarl la sesión | Cerrar para salir de la sesión: ")
    match Opcion.lower():
        case "inicio":
            while Oportunidades <= 3 and UsuarioValido == False:
                print("entre al ciclo")
                UsuarioCaptura = input("Escribe tu nombre de usuario: ")
                ContraseñaCaptura = input("Escribre tu contraseña: ")
                if Usuario == UsuarioCaptura and Contraseña == ContraseñaCaptura:
                    print("Sesión iniciada")
                    Oportunidades = 3
                    UsuarioValido = True
                    IniciarSesion = True
                    break
                else:
                    if Oportunidades <= 3:
                        print(f"Datos incorrectos. Llevas {Oportunidades} de 3")
                        Oportunidades += 1
                        if Oportunidades > 3:
                            print("has agotado tus oportunidades")
                            break
        case "cerrar":
            print("Abandonar sesión")
            break
    

 
             
