# -*- coding: utf-8 -*-
"""
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos 
se ingresan por teclado). Y los siguientes métodos:

a- El constructor.

b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo

dominio: gmail

tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email) y luego 
imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar 
la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña 
y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, como por ejemplo: informatica.fcefn@gmail.com, 
wicc2019@unsj-cuim.edu, juanLiendro1957@yahoo.com, etc.

4- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes, 
    solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta.  
    b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado. c) Construya el 
    diagrama de secuencia correspondiente.
"""
class Email:
    idCuenta=''
    dominio=''
    tipoDominio=''
    contrasena=''
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña):
        self.idCuenta = idCuenta
        self.dominio = dominio
        self.tipoDominio = tipoDominio
        self.contraseña = contraseña

    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"
    
    def getDominio(self):
        return self.dominio
    
    def crearCuenta(self, direccionCorreo):
        partes = direccionCorreo.split("@")
        if len(partes) == 2:
            idCuenta = partes[0]
            dominio_tipoDominio = partes[1]
            dominio, tipoDominio = dominio_tipoDominio.split(".")
            contraseña = input(f"Ingrese contraseña para correo {direccionCorreo}: ")
            self.idCuenta = idCuenta
            self.dominio = dominio
            self.tipoDominio = tipoDominio
            self.contraseña = contraseña
            print("Cuenta creada correctamente")
        else: 
            print("Direccion de correo incorrecta")
        return Email

"""

class Email:
    __idCuenta=''
    __dominio=''
    __tipoDominio=''
    __contrasena=''
    def __init__(self, idCuenta, dominio, tipoDominio, contrasena):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena

    def retornaEmail(self):
        return self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio
    
    def getDominio(self):
        return self.__dominio
    
#    @classmethod
    
    def crearCuenta(cls, direccionCorreo):
        partes = direccionCorreo.split('@')
        idCuenta = partes[0]
        dominio = partes[1].split('.')[0]
        tipoDominio = partes[1].split('.')[1]
        contrasena = input("Ingrese la contraseña de la cuenta: ")
        return cls(idCuenta, dominio, tipoDominio, contrasena)"
    
        """
        