# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:51:24 2021

@author: DGIP
"""

file = open("devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo valor: ")
    
for item in file:
    item = item.strip() #Eliminar espacios
    print(item)  
    
file_ok = open("devices.txt","a")

file.write(newItem)
file.close()    


