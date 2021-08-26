# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:14:43 2019

@author: CEC
"""

seq = ['soup','dog','salad','cat','great']

sseq = " ".join(seq)

filtered = lambda x: True if sseq.startswith('s') else False

filtered_list = filter(filtered, seq)

print('Words are:')
for a in filtered_list:
    print(a)