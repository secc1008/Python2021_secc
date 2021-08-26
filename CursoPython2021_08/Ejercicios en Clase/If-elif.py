# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:19:59 2021

@author: DGIP
"""

acl = int(input("Ingrese el # de ACL: "))
if acl>=1 and acl <= 99:
    print("ACL es estándar")
elif acl>= 100 and acl <= 199:
    print("ACL extendida")
else:
    print("El # ingresado no es una ACL")    