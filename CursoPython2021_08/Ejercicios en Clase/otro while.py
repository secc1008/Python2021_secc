# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:25:52 2021

@author: DGIP
"""

contar = int(input("Ingrese en # veces a contar: "))

contador = 1

while True:
    print(contador)
    contador = contador+1
    if contador>contar:
       break