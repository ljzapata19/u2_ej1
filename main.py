# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 18:52:13 2023

@author: ljzap
"""
from correo import Email 
from mensaje import imprimir_mensaje_correcto
from mensaje import imprimir_mensaje_incorrecto
from validarcorreo import validar_direccion_correo


if __name__ == '__main__':
    #Ingresar datos por teclado
    nombre = input("Ingrese su nombre: ")
    idCuenta = input("Ingrese el id de cuenta: ")
    dominio = input("Ingrese el dominio: ")
    tipoDominio = input("Ingrese el tipo de dominio: ")
    contraseña = input("Ingrese la contraseña: ")
    # Creación de instancia de la clase Email
    email = Email(idCuenta, dominio, tipoDominio, contraseña)
    
    #Imprimir Mensaje
    imprimir_mensaje_correcto(nombre, email.retornaEmail())
    
    #Modificar contraseña
    print("Cambio de contraseña")
    contraseña_Actual = input("Ingrese contraseña actual: ")
    if   contraseña_Actual == email.contraseña:
         nueva_contraseña = input("Ingrese nueva contraseña: ")
         email.contraseña == nueva_contraseña
         print("Contraseña modificada exitosamente")
    else :
         print("Contraseña incorrecta")
    
    #Crear un objeto de clase Email, a partir de una dirección de correo
    direccionCorreo = input("Ingrese direccion de correo: ")
    email.crearCuenta(direccionCorreo)
    
    #Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes, 
    #solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta
    
    import csv
    listaCorreos = []
    listaObjetos=[]
    archivo = open('archivoCorreo.csv')
    arch = csv.reader(archivo,delimiter=',')
    
    for dire in arch:
        
         if (validar_direccion_correo(dire[0])):             
             #print(f'La dirección de correo electrónico "{dire[0]}" es válida.')
             #email.crearCuenta(dire[0])
             correovalido=email.crearCuenta(dire[0])
             listaObjetos.append(correovalido)
             
             
         else:
             #print(f'La dirección de correo electrónico "{dire[0]}" no es válida.')
             imprimir_mensaje_incorrecto(dire[0])
      
    #Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al 
    #ingresado.
    
    dom_buscado=input('Ingrese dominio a buscar: ')
    cont=0
    for i in range(len(listaObjetos)):
        #listaObjetos[i].getDominio
        #correovalido=email.crearCuenta(dire[0])
        #listaObjetos.append(correovalido)
        #print('dominio:{} '.format(listaObjetos[i].getDominio))
        print('email', email.retornaEmail)
        if email.dominio == dom_buscado:
            print('ofivein')
            cont=cont+1
        
        
        #print("dominio de ",i,": ", listaObjetos[i].getDominio)
        
    print('cont: ',cont)
    
    
    
    
    
    
    
    
    
    
    
      