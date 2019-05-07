# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:27:05 2019

@author: Sahar

"""

#f = open('myfile.txt', 'w')
l = ['hi', 'there', 'I', 'am', 'writing', 'in', 'a', 'file']

'''
with open('myfile.txt', 'w') as f:
   f.read()
  
'''
with open('myfile.txt', 'w') as f:
    for s in l:
       f.write(s + '\n')
       
 

with open('myfile.txt', 'r') as f:
     for line in f:
         print(line, end='')
        

with open('myfile.txt', 'a') as f:
      f.write('Bye\n')


import os
if os.path.exists("myfile.txt"):
   os.remove("myfile.txt")
else:
    print("The file does not exist")      
      
       