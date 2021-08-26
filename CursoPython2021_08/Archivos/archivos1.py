# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:26:53 2021

@author: DGIP
"""
lista = []

file = open("devices.txt","r")
for item in file:
    item = item.strip() #Eliminar espacios
    lista.append(item)  #agregar a la lista
    print(item)
 
file.close()    

print("Lista: ",lista)
    