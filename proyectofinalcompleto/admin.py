from clasehabitacion import *
from serviadicionales import *
from clasesusuarios import *
import sqlite3
conn = sqlite3.connect('C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db') 
    
class Administrador:
            
            def __init__(self,documento,nombre,email,telefono,direccion):
                self.__documento=documento
                self.__nombre=nombre
                self.__email=email
                self.__telefono=telefono
                self.__direccion=direccion
                
                
            def consultar_Habitacion(self,conexion, d1):
                print('CONSULTA  DE HABITACIONES\n')
                print('disponibles:\n')
                consulta=Habitaciones.consultar_Habitacion (conexion, d1)
                for i in consulta:
                    print(i)
            
            def agregarHabitacion(self,conexion):
                print('AGREGAR HABITACIONES\n')
                tipo=input('¿Cual es el tipo de habitacion que deseas agregar?\n-')
                precio=input('¿Cual es el precio de la habitacion que deseas agregar?\n-')
                descripcion=input('¿Cual es la descripción de la habitación que desea agregar?\n-')
                insertar=Habitaciones.insert(conexion, tipo, precio, descripcion)
                print('Las habitaciones ahora disponibles son: ')
                consulta=Habitaciones.consultar_Habitacion(conexion, d1)
                for i in consulta:
                    print(i)
                    
            def actualizarHabitacion(self,conexion):
                print('ACTUALIZAR HABITACION\n')
                cursor=conexion.cursor()
                consulta1=Habitaciones.consultar_Habitacion(conexion)
                c1=int(input('¿Cual es el id de la habitacion por actualizar?\n-'))
                for j in consulta1:
                    if c1 in j:
                        print('Los campos actualizables son: id_habitacion,numero_habitacion,tipo_habitacion,tipocamas_habitacion,descripcion_habitacion,caracteristica_habitacion,valor_habitacion,id_tipo_habitacion')
                        campo=input('¿Cual es el campo de la habitacion que deseas actualizar?\n-')
                        d1=input('¿Cual es el nuevo dato?\n-')
                        actualizar=Habitaciones.UPDATE(conexion, campo, d1, c1)
                consulta=Habitaciones.consultar_Habitacion(conexion)
                for i in consulta:
                    print(i)
                            
            
            def eliminarHabitacion(self, conexion):
                print('ELIMINAR HABITACION')
                id_hab = int(input('¿Cual es el id de la habitacion que deseas eliminar?\n-'))
                Habitaciones.eliminar(conexion, id_hab)
                consulta = Habitaciones.consultar_Habitacion(conexion,d1)
                for i in consulta:
                    print(i)

            def consultarServicios(self,conexion):
                print('quieres CONSULTAr SERVICIOS\n')
                print('servicios disponibles:\n')
                consulta=select_Serviadicionales(conexion)
                for i in consulta:
                    print(i)
            
            def crear_Serviadicional(self,conexion):
                print('CREAR SERVICIOS')
                tipo=input('¿Cual es el nombre del nuevo servicio?\n-')
                precio=input('¿Cual es el precio del nuevo servicio?\n-')
                crear=Insert_Serviadicionales(conexion, tipo, precio)
                print()
                consulta=select_Serviadicionales(conexion)
                for i in consulta:
                    print(i)
                
            def actualizar_servicio(self,conexion):
                print('ACTUALIZAR SERVICIOS')
                print()
                consulta1=select_Serviadicionales(conexion)
                id=int(input('¿Cual es el id del servicio por actualizar?\n-'))
                for j in consulta1:
                    if id in j:
                        print('Los campos actualizables son: tiposervicio,valor_servicio')
                        campo=input('¿Cual es el nombre del campo a actualizar?\n-')
                        dato=input('¿Cual es el nuevo dato?\n-')
                        modificacion_serviadicional(conexion, campo, dato, id)
                print()
                consulta=select_Serviadicionales(conexion)
                for i in consulta:
                    print(i)
                    
            def elimiar_servicios(self,conexion):
                print('ELIMINAR SERVICIOS')
                print()
                consulta=select_Serviadicionales(conexion)
                for i in consulta:
                    print(i)
                print()
                id_servicio=int(input('¿Cual es el id_servicio  que deseas eliminar?\n-'))
                eliminar=eliminacion_serviadicional(conexion, id_servicio)
                print()
                consulta1=select_Serviadicionales(conexion)
                for j in consulta1:
                    print(j)
                
            
            def consulta_de_empleados(self,conexion):
                print('CONSULTAR EMPLEADOS')
                print()
                print('El personal del hotel, y los clientes son:\n')
                consulta=seleccionar_usuario(conexion)
                for i in consulta:
                    print(i)
                
            def crear_usuarios(self,con):
                print('CREAR NUEVOS USUARIOS')
                print()
                print('DATOS NUEVOS DE USUARIO')
                print()
                print('TIPO USUARIOS\n 1.Administrador \n 2.Clientes \n 3.Recepcionista \n 4.Mesero \n 5.RoomServive\n')
                id_usuario=int(input('¿Cual es el documento del nuevo usuario?\n-'))
                nombre_usuario=input('¿Cual es el nombre del nuevo usuario?\n-')
                apellido_usuario=input('¿Cual es el apellido del nuevo usuario?\n-')
                email_usuario=input('¿Cual es el email del nuevo usuario?\n-')
                direccion_usuario=input('¿Cual es la direccion del nuevo usuario?\n-')
                telefono_usuario=input('¿Cual es el telefono del nuevo usuario?\n-')
                pass_usuario=input('¿Cual es la contraseña del nuevo usuario?\n-')
                fecharest_usuario=input('¿Cual es la fecha de restablecimiento de contraseña del nuevo usuario?\n-')
                fechareg_usuario=input('¿Cual es la fecha de registro del nuevo usuario?\n-')
                id_tipo_usuario=int(input('¿Que tipo de usuario es el nuevo usuario?(id)\n-'))
                crear=insertar_USUARIO(con, id_usuario, nombre_usuario, apellido_usuario, email_usuario, telefono_usuario, direccion_usuario, pass_usuario, fecharest_usuario, fechareg_usuario, id_tipo_usuario)
                consulta=(con,id)
                for i in consulta:
                    print(i)
                print()
                    
            def actualizar_usuarios(self, conexion):
                print('ACTUALIZAR USUARIOS')
                print()
                consulta1 = seleccionar_usuario(conexion)
                id_usuario = int(input('¿Cual es el documento del usuario por actualizar?\n-'))
                for j in consulta1:
                    if id_usuario in j:
                        tabla= input('¿Cual es el nombre de la tabla que va a actualizar?\n-')
                        print('Los campos actualizables son: nombre_usuario, apellido_usuario, email_usuario, direccion_usuario, telefono_usuario, pass_usuario, fecharest_usuario, fechareg_usuario, id_tipo_usuario')
                        campo = input('¿Cual es el nombre del campo a actualizar?\n-')
                        dato = input('¿Cual es el nuevo dato?\n-')
                        modificar(conexion, tabla, campo, dato, id_usuario)
                print()
               
            
            def eliminar_usuario(self,conexion):
                print('ELIMINAR USUARIOS')
                print()
                tabla= input('¿Cual es la tabla  que deseas mirar?\n-')
                campo=input('¿Cual es el nombre del campo para mirar?\n-')
                dato= input('¿Cual es el nombre del dato para eliminar?\n-')
                condition=int(input('¿Cual es el id o documento del usuario que deseas eliminar?\n-'))
                eliminar=eliminar_usuario(conexion,tabla, campo, dato,condition)
                print()
        #Ejemplo
n2=Administrador(21312312,'neimar', 'wdqdw@gmail.com', 3123213, 'calle2')
d1 = n2
"""n2.consultar_Habitacion(con, d1)
n2.agregarHabitacion(con)
n2.eliminarHabitacion(con)
n2.consultarServicios(con)
n2.crear_Serviadicional(con)
n2.actualizar_servicio(con)
n2.elimiar_servicios(con)
n2.consulta_de_empleados(con)
n2.crear_usuarios(con)
n2.actualizar_usuarios(con)
n2.eliminar_usuario(con)"""