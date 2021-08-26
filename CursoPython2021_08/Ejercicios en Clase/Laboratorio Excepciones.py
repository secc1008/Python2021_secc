# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:01:46 2021

@author: DGIP
"""

def readint(prompt, min, max):
#
# put your code here
#     

    while True:
        try:
            num = int(input("Ingrese un número: "))
   



    try:
        prompt = int(input("Ingrese un número: "))
        y = prompt
        print(y)
        min=-10
        max=10
        if y <=10 or y >-10:            
            raise Exception('x should not exceed 5. The value of x was: {}'.format(y))
        else:    
            print("Intenta de nuevo")
              



v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
