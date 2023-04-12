from crudreserva import *
from random import *

class Cliente:
    def __init__(self,Nombre,TDocumento,NDocumento,correo,Ntelefono,direccion):
        self.Nombre=Nombre
        self.TDocumento=TDocumento
        self.Documento=NDocumento
        self.correo=correo
        self.Ntelefono=Ntelefono
        self.direccion=direccion
    def registrar(self,conexion):
        print("REGISTRAR")
        fechall=input("Ingresa la fecha de tu ingreso: ")
        fechasalida=input("Cuando tienes planiado salir?:")
        precio=randint(100000,1800000)
        Registro=insertarr(conexion,fechall,fechasalida,precio)
        for i in Registro:
            print(i)
    def ConsultarR(self,conexion):
        print("Consultar tipos de reservas")
        print("Las reservas son:")
        consultarR=leer(conexion)
        for i in consultarR:
            print(i)
    def Actualizar(self,conexion):
        print("Se actualizara una reserva")
        id=input("Digita el id de la reserva que vas actualizar:")
        print("Solo puedes actualizar la fecha")
        act=input("Entonces quieres actualizar,Fechaingre_reserva o Fechasali_reserva")
        if act!="Fechaingre_reserva":
            print("No se puede actualizar este campo")
        elif act!="Fechasali_reserva":
            print("No puedes actualizar este campo")
        else:
            dato=input("Ingresa el dato que deseas actualizar:")
            Actualizarr=modificar(conexion,act,dato,id)
    def canselar(self,conexion):
        print("Eliminar reserva")
        print("Lista de reservas:")
        reservas=leer(self,conexion)
        for i in reservas:
            print(i)
        canselar=int(input("Ingresa el id de la reserva a eliminar,si elijiste la opcion que no era espicha -1:"))
        for lu in reservas:
            if canselar in lu:
                canselar1=eliminar(conexion,canselar)
                break
            else:
                print("Saliste de la opcion")
                break

ob=Cliente("luz","CC",1015849205,"correo@gmail.coom",3015205498,"cll 45 sur")  
ob.ConsultarR(con)     
ob.Actualizar(con)
ob.canselar(con)  
            