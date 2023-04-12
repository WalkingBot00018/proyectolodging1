from facturacion import *
from reserva import *
import sqlite3

with sqlite3.connect('C:\\Ducuara1\\db\\proyectolodging\\lodging2.0.db')as con:
    micursor=con.cursor()

    class recepcionista:
        def __init__(self, documento,nombre,email,telefono,direccion):
            self.documento = documento
            self.nombre = nombre
            self.email = email
            self.telefono = telefono
            self.direccion = direccion

        def crear_reserva(self,con):
            print('CREAR RESERVA')
            print('Datos de la nueva reserva')
            b1=int(input('¿Id de la reserva?\n-'))
            b2=int(input('¿Id de la habitacion?\n-'))
            b3=int(input('¿Id usuario?\n-'))
            b4=(input('¿Tipo de reserva?\n-'))
            b5=input('¿Cual es la fecha de llegada de la nueva reserva?\n-')
            b6=input('¿Cual es la fecha de salida de la nueva reserva?\n-')
            b7=input('¿Motivo de alojamiento?\n-')
            b8=int(input('¿Id tipo Reserva?\n-'))
            crear=insertar_reserva(con, b1, b2, b3, b4, b5, b6, b7, b8)
            print()
            consulta=consultarReservaUsuario(con,b4)
            for i in consulta:
                print(i)
            print()

        def consultar_reserva(self,conexion):
            print('CONSULTAR RESERVA')
            d1=int(input('¿Cual es tu documento?\n-'))
            consulta=consultarReservaUsuario(conexion, d1)
            print('Tus reservas son:')
            for i in consulta:
                print(i)
            print()

        def actualizarReserva(self,con):
            print('ACTUALIZAR RESERVA')
            print()
            c1=int(input('¿Cual es el id de la reserva que deseas actualizar?\n-'))
            print('Los campos actualizables son: \ntipo_reserva \nFechaSalida_res \nalojaminto_reserva\n')
            val2=input('¿Cual es el campo de la reserva que deseas actualizar?\n-')
            d1=input('¿Cual es el nuevo dato?\n-')
            modificar=modificar_reserva(con, val2, d1, c1)
            consulta=consultarReservar(con, c1)
            for i in consulta:
                print(i)
            print()
        
        def eliminar_reserva(self,conexion):
            micursor=con.cursor()
            print('ELIMINAR RESERVA')
            d1=int(input('¿Cual es el id de la reserva que deseas eliminar?\n-'))
            eliminar=eliminar_reserva(conexion, d1)
            print()
            consulta=consultarReservaUsuario(conexion, d1)
            for i in consulta:
                print(i)
            print()

        def consultarFactura(self,conexion):
            print('CONSULTAR FACTURA')
            print()
            d1=(input('¿Cual es el id del usuario?\n-'))
            consulta=consultarReservaUsuario(conexion, d1)
            print('Sus facturas son:')
            for i in consulta:
                print(i)
            print()

ob1=recepcionista(542313234,'santiago','santiago@gmail.com',64532321,'calle 34c ')
'''ob1.consultar_reserva(con)'''
#ob1.crear_reserva(con)
'''ob1.actualizarReserva(con)'''
ob1.eliminar_reserva(con)
#ob1.consultarFactura(con)