# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:59:29 2026

@author: Augusto Lorenzo Gassós
"""

Opcion = "e"

match Opcion:
    case "a":
        print("Menu a")
    case "b":
        print("Menu b")
    case "c":
        print("Menu c")
    case _:
        print("Menu no identificado")
   
dia = "Sábado"
match dia:
    case "Lunes" | "Martes" | "Miércoles" | "Jueves" | "Viernes":
        print("día de la semana")
    case "Sábado" | "Domingo":
        print("Fin de semana")
    case _:
        print("Día no reconocido")

Coordenadas = (10,5)

match Coordenadas:
    case (0,0):
        print("Origen")
    case (x,0):
        print("Eje x")
    case (0,y):
        print("Eje y")
    case (x,y):
        print(f"Punto general ({x}, {y})")
    case _:
        print("Coordenadas incorrectas")
        
Entrada = "55112816361"
Entrada2="asvqere"
Entrada3="asxeb123."
Entrada.isdigit()
print(Entrada.isdigit())    
Entrada2.isalpha()
print(Entrada2.isalpha())   
Entrada3.isalnum()
print(Entrada3.isalnum())   

if Entrada.isdigit() and len(Entrada) == 10:
    print("Número de celular correcto")
else:
    print("Número de celular invalido")

Contraseña = "cjineci"
ContraseñaGuardada = "cjineci"
Correo = "algo@hotmail.com"
CorreoGuardado = "Algo@hotmail.com"

if Contraseña == ContraseñaGuardada and Correo.upper() == CorreoGuardado.upper():
    print("Se ingresa al sistema")
else:
    print("ingreso  no valido")

if "@" in Correo and "." in Correo and ("gmail" in Correo or "hotmail" in Correo):
    print("Correo valido")
else:
    print("Correo invalido")
    


 

  