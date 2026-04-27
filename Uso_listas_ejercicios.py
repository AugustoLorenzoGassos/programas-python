# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:00:14 2026

@author: Augusto Lorenzo Gassós
"""

Lista1 = ["a","b","c",1,2,3,4,True,False,5.7]

#Añadir elementos a la lista
Lista1.append("A")
Lista1.append("B")

#Elemento = input("Agrega un elementoa la lista: ")
#Lista1.append(Elemento)

print(Lista1)
print(Lista1[7])

Lista1[0]="R"

print(Lista1)

A = Lista1[1]
print(A)

#try:
#    :IndexError
#        print("Índice fuera de rango")