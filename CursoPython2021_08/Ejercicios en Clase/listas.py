# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:57:00 2021

@author: DGIP
"""

lista = ["R1","R2","R3","S1","S3"]

print("Antes del FOR")
for j in lista:
    print(j)
    print("dentro del FOR")
print ("Fuera FOR")








lista = ["R1","R2","R3","S1","S3"]


for j in lista:
    if "R" in j:
        print(j)




lista1 = []
lista2 = []
lista = ["R1","R2","R3","S1","S3"]
for i in lista:
    if "S" in i:    
        lista1.append(i)
        print("Lista1: ",lista1)
    elif "R" in i:
        lista2.append(i)        
        print("Lista2: ",lista2)
