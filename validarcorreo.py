# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:19:04 2023

@author: ljzap
"""
import re
def validar_direccion_correo(dire):
    # Crear una expresión regular para validar correos
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verificar si el correo coincide con el patrón
    if re.match(patron, dire):
        return True
    else:
        return False
    