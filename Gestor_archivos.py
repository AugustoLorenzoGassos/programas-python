# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 17:39:47 2026

@author: Giovanny
"""
import os
#Gestor de archivos 
#menu interactivo

#1.generar carpeta, Creara una carpeta en el repositorio actal
    #Si ya extiste, mandar la indicacion al ususario, de lo contrario
    #la generar
#2.Eliminar una carpeta.
    #Si no existe, mandar indicacion al usuario, de lo contrario
    #la eliminara
    
#3.Generar archivo en carpeta especifica
#     Si no existe, indicar al usuario y preguntar si quiere generar 
#     tanto la carpeta como el archivo (Carpetas anidadas)
#4.renombrar archivo y carpeta
#   Renombrar un archivo y carpeta 



while True:
    print("\n1.generar carpeta\n2.Eliminar una carpeta\n3.Generar archivo\n4.renombrar archivo y carpeta")
    eleccion = input("Ingresa una de las 4 opciones: ")
    match eleccion:
        case "1":
            print("Generar carpetas")
            nueva_car = input("Nombre de la nueva carpeta")
            if not os.path.exists(nueva_car):
                os.mkdir(nueva_car)
                print("Generada correctamente")
                
            else:
                print("La carpeta denominada",nueva_car,"ya existe.")
                
        case "2":
            print("Eliminar carpetas")
            elimi_car = input("Nombre de la carpeta a eliminar: ")
            if not os.path.exists(elimi_car):
                print("La carpeta",elimi_car,"no fue encontrada")
            else:
                os.rmdir(elimi_car)
                print("Eliminado correctamente")
                
        case "3":
            print("Generar archivo")
            car = input("A que carpeta se realizara el archivo: ")
            archivo = input("nombre der archivo a generar: ")
            
            if not os.path.exists(os.path.join(car,f"{archivo}.txt")):
                os.path.join(car,f"{archivo}.txt")
                print("Generados correctamente")
                
            else:
                print("La carpeta y archivo ya existe")
                
                
        case "4":
            print("renombrar")
            car_r = input("A que carpeta se realizara el archivo: ")
            archivo_r = input("nombre del archivo a renombrar: ")
            archivo_nuevo = os.path.join(car_r, "archivo_nuevo.txt")
            os.rename(archivo_r, archivo_nuevo)
            
        case _:
            break












