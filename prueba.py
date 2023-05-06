# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:06:56 2023

@author: ljzap
"""

import csv

# opening the CSV file
#with open('archivoCorreo.csv', mode ='r')as file:
file = open('archivoCorreo.csv')   

# reading the CSV file
csvFile = csv.reader(file,delimiter=',')
# displaying the contents of the CSV file
for lines in csvFile:
  print(lines[0])
  
  
  
  """
  
    import csv
    listaCorreos = []
    archivo = open('archivoCorreo.csv')
    arch = csv.reader(archivo,delimiter=',')
    
    for dire in arch:
        
         if (validar_direccion_correo(dire[0])):             
             #print(f'La dirección de correo electrónico "{dire[0]}" es válida.')
             email.crearCuenta(dire[0])
             
         else:
             #print(f'La dirección de correo electrónico "{dire[0]}" no es válida.')
             imprimir_mensaje_incorrecto(dire[0])
  
  
  
  """