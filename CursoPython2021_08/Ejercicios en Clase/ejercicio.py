# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:19:19 2021

@author: DGIP
"""
milla = float(1609.344)
km = milla/1000
galon = 3.785411784


def l100kmtompg(litros):
    
    return((1/((litros * galon) / km ))) * 100

lista1 = [3.9,7.5,10]
for n in lista1:
    print(n,l100kmtompg(n))

 
     




def mpgtol100km(millas):
    
    return((1/((millas * km) / galon)))*100

lista2 = [60.3114,31.3619,23.5214]
for i in lista2:
    print(i,mpgtol100km(i))
    
    