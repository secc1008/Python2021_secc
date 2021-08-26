# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:02:12 2021

@author: DGIP
"""

# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( "Lista de Países: " ,country )
print( "Diccionario de Capitales: ", capitals)
print( "2do valor clave sudáfrica: ", capitals["South Africa"][1])
print(capitals[4])

print( "2do valor clave sudáfrica: ", capitals["South Africa"])

What response did you get?
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""

print( capitals["South Africa"[1]] )
"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""
