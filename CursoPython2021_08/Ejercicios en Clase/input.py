# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:33:14 2021

@author: DGIP
"""

primerNombre = input("Ingresa tu nombre: ")

apellido = input("Ingresa tu apellido: ")

dirección = input("Ingresa tu dirreción: ")
                  
edad = int(input("Ingresa tu edad: "))



print ("Hola: ", primerNombre, " ", apellido)

print ("Dirección: ", dirección)

if edad >=1 and edad <=12:
    print("Es niño/a")
elif edad >=13 and edad <=17:
    print("Es adoloscente")    
elif edad >=18 and edad <= 25:
    print("Es joven")  
elif edad >=26 and edad <= 59:
    print("Es adulto") 
elif edad >=60 and edad <= 100:
    print("Es adulto mayor")     
else: 
    print ("Edad incorrecta")    
    

print ("Edad:", edad)

print ("Registro correcto !! Bienvenido: ", primerNombre, apellido, edad, "años" )