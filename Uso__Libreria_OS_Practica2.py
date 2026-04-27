# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 18:07:50 2026

@author: Augusto Lorenzo Gassós
"""

import datetime
import os

Contador = 0

with open("logs.txt", "w", encoding="UTF-8") as Logs:
    while Contador < 5:
        FechaAcutual = datetime.datetime.now()
        match os.path.exists("logs"):
            case False:
                os.mkdir("logs")
                print("La carpeta no existe. Creada.", file = Logs)
            case True:
                print(f"La carpeta ya existe. Fecha del  monitoreo {FechaAcutual}", file = Logs)
        Contador += 1
    
    print(f"Fin del monitoreo {datetime.datetime.now()}", file = Logs)