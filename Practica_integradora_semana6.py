# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 18:07:53 2026

@author: Augusto Lorenzo Gassós
"""

#Correo de 8 a 10 elementos mínimo
#Debe de contener @, . y organización
#Contener tipo de correo .com .edu. . gob .mx

#Contraseña
#Mínimo de 8 caracteres
#Un elemento especial
#Numéricos del 0 al 9

#Solicitar un usuario y contraseña para registro
#En caso de ser válidos, guardarlos
#En caso contrario inidcar el error}
#Después de guardar, solicitarlo. Si son coincicentes, indicarlo
#Guardar el usuario y contraseña en un archivo de texto

Correo = input("Ingresa tu cuenta de correo de regito:")
Contraseña = input("Ingresa tu contraseña de registro:")

CorreoGuardado=""
ContraseñaGuardada=""

CorreoValido = False
ContraseñaValida = False


#Validación del correo
if len(Correo)<8:
    print("La longitud del correo debe de ser de al menos 8 caracteres")
else:
    if "@" not in Correo and "." not in Correo:
        print("El correo debe de contener los siguentes caracteres: @, .")
    else:
        if "gmail" not in Correo and "hotmail" not in Correo and "yahoo" not in Correo:
            print("EL correo debe de contar con un proveedor válido")
        else:
            if ".gob" not in Correo and ".edu" not in Correo and ".mx" not in Correo and ".com" not in Correo:
                print("El correo debe de pertenecer a una organización válida")
            else:
                print("Correo válido")
                CorreoValido = True
                CorreoGuardado = Correo
#Validación de la contraseña
if len(Contraseña)<8:
    print("La contraseña no puede tener menios de 8 caracteres")
else:
    if "#"  not in Contraseña and "@" not in Contraseña and "$" not in Contraseña:
        print("La contraseña debe de incluir un caracter especial")
    else:
        if "1" not in Contraseña and "2" not in Contraseña and "3" not in Contraseña and "4" not in Contraseña:
            print("la contraseña debe de in,cuir un número")
        else:
            print("Contreña válida")
            ContraseñaValida = True
            ContraseñaGuardada = Contraseña

if CorreoValido == True and ContraseñaValida == True:
    print("Iniciar la sesión")
    Correo = input("Escribre el correo con el que realizaste tu registro:")
    Contraseña = input("Escribe la contraseña con la que te registraste:")
    if Correo == CorreoGuardado and Contraseña == ContraseñaGuardada:
        print("Inicio de sesión correcto")
    else:
        print("Error al ingresar tus credenciales")
else:
    print("No lograste realizar tu registro de forma correcta")

with open("c:/Diplomado Python/InicioSesion.txt","a") as f:
        print("Datos de inicio de sesión", file=f)
        print(f"{'Usuario':<20}{Correo:<14}", file=f)
        print(f"{'Contraseña':<20}{Contraseña:<14}", file=f)




            

