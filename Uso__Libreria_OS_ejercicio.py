# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 17:40:02 2026

@author: Augusto Lorenzo Gassós
"""
#Gestor de carpetas y documentos

#1. Generar carpeta. Crear una carpeta en el repositorio actual
    #Si ya existe mandar la indicación al usuario. de lo conttrario crerar la carpeta
#2. Eliminar una carpeta. Se eliminará la carpeta
    #Si no existe mandar la indicaciópn al usuaro. De lo contrario eliminar la carpeta
#3. Generar un archivoi en una caprta en específico
    #Si no existe, indicar al usuario y preguntar si quiere generr tanto la carpeta como el archivo
#4. Reombrar carpetas y archivos

import os

Opcion = ""
NombreCarpeta = ""
NombreCarpetaActual = ""
NombreArchivo = ""
CrearCarpeta = ""

print("\n GESTOR DE CARPETAS Y DOCUMENTOS\n")
print("V. Visualizar contenido de la carpeta")
print("1. Crear carpeta")
print("2. Eliminar carpeta")
print("3. Generar archivo")
print("4. Renombrar carétas/documentos")
print("5. Salir")

while True:

    Opcion = input("\nEscriba el número de la opción deseada: ")
   
    match Opcion:
        case "V":
            print(os.listdir('.'))
        case "1":
            NombreCarpeta = input("Escribe el  nombre de la carpeta: ")
            if "." in NombreCarpeta or len(NombreCarpeta) == 0:
                print("Nombre de la carpeta vacío o invalido")
            else:
                if os.path.exists(NombreCarpeta):
                    print(f"La carpeta {NombreCarpeta} ya existe")
                else:
                    os.mkdir(NombreCarpeta)
                    print(f"La carpeta {NombreCarpeta} fue removida con éxito")
        case "2":
            NombreCarpeta = input("Escribe el  nombre de la carpeta: ")
            if len(NombreCarpeta) == 0:
                print("El nombre de ka carpeta no puede estar vacío")
            else:
                if not os.path.exists(NombreCarpeta):
                    print(f"La carpeta {NombreCarpeta} no existe")
                else:
                    os.rmdir(NombreCarpeta)
        case "3":
            NombreCarpeta = input("Escriba el nombre de la carpeta donde se va a crear el documento: ")
            NombreArchivo = input("Escrtiba el nombre del archivo: ")
            if len(NombreCarpeta) == 0 or len(NombreArchivo)==0:
                print("Los nombres, tanto de la carpeta como del documento, no puede estar vacíos")
            else:
                if not os.path.exists(NombreCarpeta):
                    CrearCarpeta = input("¿Deseas c rear la carpate (S/N?")
                    if CrearCarpeta == "S":
                        os.mkdir(NombreCarpeta)
                        ArchivoCrear = os.path.join(NombreCarpeta, NombreArchivo)  
                        with open(ArchivoCrear, 'w') as f:
                            f.write("Este es el texto de prueba para crear el documento")
                    else:
                        print("La carpeta debe de existir para crear el docuemto")
        case "4":
            NombreCarpeta = input("Escribe el  nombre de la carpeta a la que se le va a cambiar el nombre: ")
            NombreCarpetaActual = input("Escribe el nombre definitivo de la carpeta: ")
            if len(NombreCarpeta)==0 or len(NombreCarpetaActual)==0:
                print("Los nombres no pueden quedar vacío")
            else:
                os.rename(NombreCarpeta,NombreCarpetaActual)
        case "5":
            break

    
