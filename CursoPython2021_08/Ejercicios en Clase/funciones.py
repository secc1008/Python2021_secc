# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:12:21 2021

@author: DGIP
"""

def mensaje():
    print ("Ingrese un número: ")
    
mensaje();
a = input();

mensaje();
b = input();

mensaje();
c = input();


mensaje();
d = input();
   
print ("Numeros: ", a,b,c,d)



"""Otra función"""

def saludo(nombre):
    print("Hola: ", nombre)
    
saludo("Sara")
saludo("Elisa")
    
"""Otra función"""

def saludo2(nombre1,nombre2):
    print ("Hola.. ", nombre1)
    print ("Hola.. ", nombre2)
    
saludo2("Sara", "Cruz")   
saludo2("Sofia", "Salome")  
saludo2("Emma", "Sofía")   

"""Otra función"""

def direcciones(ciudad, barrio, calle):
    print("Su dirección de referencia es")
    print("Su ciudad es: ", ciudad)
    print("Su barrio es: ", barrio)
    print("Su calle es: ", calle)
    
ciu = input("Ingrese la ciudad: ")
bar = input("Ingrese el barrio de referencia: ")
cal = input("Ingrese la calle para entrega de su pedido: ")
    
direcciones(ciu, bar, cal)
    

"""Otra función"""

def resta(a,b):
    print(a-b)
    
resta(3,2)
resta(2,3)
resta(a=3,b=2)
resta(3,b=2)   
    
