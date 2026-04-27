# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 16:07:08 2025

@author: Augusto Lorenzo Gassós
"""

Edad=18
if Edad<18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
    
Edad=None
if Edad:
    print("Eres menor de edad")
else:
    print("No puedes dejar los camnpos vacios")
    
#< que 0 = Mucho frío
# 0 - 10 frío
#10 - 20 fresco
#>20

Temperatura = 30
if Temperatura < 0:
    print("Mucho frío")
else:
    if Temperatura<10:
        print("frío")
    else:
        if Temperatura<20:
            print("Fresco")
        else:
            print("Normal")
#>=60 Aprobado
#<60 Reprobado
#>=90 Alumno excelente
#>=75 Aprobado con buen desempeño
#>=60 Aprobado con lo justo   
#<0
#>100
        
Nota1=60
Nota2=70
Nota3=70
Promedio=(Nota1+Nota2+Nota3)/3
if Promedio>=60:
    if Promedio>=90:
        print("Alumno excelente")
    elif Promedio>=75:
        print("Alumno arobado con buen desempeño")
    else:
        print("Alunmno aprbado con lo justo")
else:
    print("Alumno reprobado")
    
Nota1=60
Nota2=60
Nota3=60
Promedio=(Nota1+Nota2+Nota3)/3
if Promedio>0:
    if Promedio<=100:
        if Promedio>=60:
            if Promedio>=90:
                print("Alumno excelente")
            elif Promedio>=75:
                print("Alumno aptobado con buen desempeño")
            else:
                print("Alumno aprbado con lo justo")
        else:
            print("Alumno reprobado")
    else:
        print("El promedio no puede ser mayor que 1000")
else:
    print("No puedes generar un promedio menor a cero")
      
Temperatura=30
if Temperatura <0:
    print("Mucho frío")
elif Temperatura<10:
    print("Frío")
elif Temperatura<20:
    print("Fesco")
elif Temperatura<30:
    print("Normal")
else:
    print("Caliente")
    

Nota1=89
Nota2=80
Nota3=80
Promedio=(Nota1+Nota2+Nota3)/3
if Promedio>0:
    if Promedio<=100:
        if Promedio>=60:
            if Promedio>=90:
                print("Alumno excelente")
            elif Promedio>=75:
                print("Alumno aprobado con bien desempeño")
            else:
                if Promedio>=60:
                    print("Alumno aprobado con lo justo")
                else:
                    if Promedio>0:
                        print("Alumno reprobado")
                    else:
                        print("Calificación no valida. No puede ser meno que 0")


