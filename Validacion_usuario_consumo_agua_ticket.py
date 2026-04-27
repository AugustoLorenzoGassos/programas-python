# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:38:19 2026

@author: Augusto Lorenzo Gassós
"""

import datetime

NombreUsuario = ""
NumeroUsuario = ""

ConsumoM3 = 0
ConsumoBase = 0
ConsumoExtra = 0

ImporteConsumo = 0
ImporteConsumoBase = 0
ImporteConsumoExtra = 0
DescuentoConsumo = 0

TarifaBase = 5
TarifaExtra = 8
AplicarDescuento = False
Folio = "TX-2025-00097"

NombreUsuario = input("Escibre el nombre del udsuario: ")
NumeroUsuario = input("Escribe el numero del cliente: ")
ConsumoM3 = float(input("Cantidad de metros cúbucos utilizados en el periodo: "))

if ConsumoM3 < 0:
    raise ValueError("el consumo no puede ser negativo")
else:
    if ConsumoM3 <= 50:
        ImporteConsumo = ConsumoM3 * TarifaBase
        if ConsumoM3 < 20:
            AplicarDescuento = True
            ImporteConsumo = ImporteConsumo - (ImporteConsumo * .20)
    else:
        ImporteConsumo = 250 + ((ConsumoM3 - 50)*8)
    print(f"Usuario: {NombreUsuario}")
    print(f"El consumo total fue: {ConsumoM3}")
    print(f"El importe a cubrir es: {ImporteConsumo}")
    if AplicarDescuento == True:
        print("Aplicar descuento: Sí")
    else:
        print("Aplicar descuento: No")
    
#Parte 2

Hoy = datetime.datetime.now().strftime("%d/%m/%y")
Hora = datetime.datetime.now().strftime("%H:%M:%S")
if ConsumoM3 > 50:
    ConsumoBase = 50
    ImpoteConsumoBase = 50 * 5
    ConsumoExtra = ConsumoM3 - 50
    ImporteConsumoExtra = ConsumoExtra * 8
else:
    ImpoteConsumoBase = ConsumoM3 * 5
    if ConsumoM3 < 20:
        DescuentoConsumo = ImpoteConsumoBase * .20 

print("="*48)
print("\nAGUA Y SERVICIOS CETEC S.A. DE C.V.".center((48)))
print("Av Ficticia 123 Col. Cenrtro, Ciudad Ejempo".center((48)))
print("RFC: CET200101ABC".center((48)))
print("Tel: (55) 1234-5678".center((48)))
print("www: cetec-servicios.mx")
print("="*48)
print(f"\nFolio {Folio} Fecha {Hoy}")
print(f"Hora: {Hora}")

print("-"*48)
print(f"Cliente: {NombreUsuario}" )
print(f"Número de cliente: {NumeroUsuario}")
print("-"*48)
print(f"{'Descripción':^21}{'Precio':^9}{'Cantidad':^9}{'Total':^9}")
print(f"{'Consumo total m3':<21}{ConsumoM3:^9}{'1':^9}{ConsumoM3:>9}")
print(f"{'Tarifa base 50m3 * 5':<21}{ImpoteConsumoBase:^9.2f}{'1':^9}{ImpoteConsumoBase:^9.2f}")
print(f"Tarifa extra {ConsumoExtra}m3 * 8{ImporteConsumoExtra:^9.2f}{'1':^9}{ImporteConsumoExtra:^9.2f}")
print(f"Descuento por bajo consumo{DescuentoConsumo:^9.2f}{'1':^9}{DescuentoConsumo:^9.2f}")
print("-"*48)
print(f"Subtotal{(ImpoteConsumoBase + ImporteConsumoExtra - DescuentoConsumo):>40.2f}")
print(f"IVA (16%) {(ImpoteConsumoBase + ImporteConsumoExtra - DescuentoConsumo)*.16:>38.2f}")
print(f"TOTAL {(ImpoteConsumoBase + ImporteConsumoExtra - DescuentoConsumo)+((ImpoteConsumoBase + ImporteConsumoExtra - DescuentoConsumo)*.16):>42.2f}")
print("="*48)
print("Método de pago:".ljust(24),"Tarjeta de débito".rjust(24))
print("Observaciones".ljust((24)),"Pago recibido con éxito".rjust(24))
print("="*48)
print("Gracias por su preferencia".center((48)))
print("Conserve este comprobanyte como constancia de pago")
print("="*48)









