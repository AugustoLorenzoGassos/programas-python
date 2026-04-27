# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 17:25:32 2026

@author: Giovanny
"""

# =========================================
# LIBRERÍA OS EN PYTHON
# EJEMPLOS CORTOS EN UN SOLO ARCHIVO
# =========================================

import os

# -------------------------------------------------
# 1) Ver el directorio actual
# -------------------------------------------------
print("1) Directorio actual:")
print(os.getcwd())

# -------------------------------------------------
# 2) Listar archivos y carpetas del directorio
# -------------------------------------------------
print("\n2) Contenido del directorio actual:")
print(os.listdir("."))


# -------------------------------------------------
# 3) Crear una carpeta
# -------------------------------------------------

print("\n3) Crear carpeta 'mi_carpeta'")
if not os.path.exists("mi_carpeta"):
    os.mkdir("mi_carpeta")
    print("Carpeta creada")
else:
    print("La carpeta ya existe")


# -------------------------------------------------
# 4) Crear carpetas anidadas
# -------------------------------------------------
print("\n4) Crear carpetas anidadas")
ruta_anidada = os.path.join("mi_carpeta", "sub1", "sub2")
if not os.path.exists(ruta_anidada):
    os.makedirs(ruta_anidada)
    print("Carpetas anidadas creadas")


# -------------------------------------------------
# 5) Crear un archivo de texto
# -------------------------------------------------
print("\n5) Crear archivo de texto")
archivo = os.path.join("mi_carpeta", "archivo.txt")


with open(archivo, "w") as f:
    f.write("Archivo de prueba para la librería os")


# -------------------------------------------------
# 6) Verificar si existe una ruta
# -------------------------------------------------
print("\n6) Verificar existencia del archivo")
print(os.path.exists(archivo))


# -------------------------------------------------
# 7) Verificar si es archivo o carpeta
# -------------------------------------------------
print("\n7) Tipo de ruta")
print("Es archivo:", os.path.isfile(archivo))
print("Es carpeta:", os.path.isdir("mi_carpeta"))



# -------------------------------------------------
# 11) Renombrar archivo
# -------------------------------------------------
print("\n11) Renombrar archivo")
archivo_nuevo = os.path.join("mi_carpeta", "archivo_nuevo.txt")
os.rename(archivo, archivo_nuevo)


# -------------------------------------------------
# 12) Información del archivo
# -------------------------------------------------
print("\n12) Información del archivo")
info = os.stat(archivo_nuevo)
print("Tamaño (bytes):", info.st_size)


# -------------------------------------------------
# 14) Usuario del sistema
# -------------------------------------------------
print("\n14) Usuario del sistema")
try:
    print(os.getlogin())
except:
    print("No disponible en este entorno")


# -------------------------------------------------
# 15) Núcleos del procesador
# -------------------------------------------------
print("\n15) Núcleos del procesador")
print(os.cpu_count())


# -------------------------------------------------
# 16) Recorrer carpetas con os.walk
# -------------------------------------------------
print("\n16) Recorrer carpetas con os.walk")
for ruta, carpetas, archivos in os.walk("mi_carpeta"):
    print("Ruta:", ruta)
    print("Carpetas:", carpetas)
    print("Archivos:", archivos)


# -------------------------------------------------
# 17) Ejecutar comando del sistema
# -------------------------------------------------
print("\n17) Ejecutar comando del sistema")
os.system("dir")      # Windows
# os.system("ls")     # Linux / Mac


# -------------------------------------------------
# 18) Eliminar archivo
# -------------------------------------------------
print("\n18) Eliminar archivo")
os.remove(archivo_nuevo)


# -------------------------------------------------
# 19) Eliminar carpetas (de adentro hacia afuera)
# -------------------------------------------------
print("\n19) Eliminar carpetas")
os.rmdir(os.path.join("mi_carpeta", "sub1", "sub2"))
os.rmdir(os.path.join("mi_carpeta", "sub1"))
os.rmdir("mi_carpeta")


# -------------------------------------------------
# FIN
# -------------------------------------------------
print("\n--- FIN DE LA DEMOSTRACIÓN ---")
