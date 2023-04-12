from crudservicios import *
import sqlite3

with sqlite3.connect('C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')as con:
    micursor=con.cursor()

    class servicio:
        def __init__(self, id_servicio, tiposervicio, valor_servicio):
            self.id_servicio = id_servicio
            self.tiposervicio = tiposervicio
            self.valor_servicio = valor_servicio

        def agregar_servicio(self, conexion):
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO serviadicional VALUES ( ?, ?, ?)',
                           (self.id_servicio, self.tiposervicio, self.valor_servicio))
        
            conexion.commit()

        def actualizar_servicio(self, conexion,id_servicio, tiposervicio, valor_servicio):
            cursor = conexion.cursor()
            cursor.execute('UPDATE serviadicional SET id_servicio=?, tiposervicio=?, valor_servicio=? WHERE id_servicio=?',
                        (id_servicio, tiposervicio, valor_servicio, id_servicio))
            conexion.commit()
            if cursor.rowcount > 0:
                return "El servicio ha sido actualizado."
            else:
                return "No se ha encontrado el servicio con el id especificado."
            

        def cancelar_servicio(self, conexion):
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM serviadicional WHERE id_servicio=?', (self.id_servicio,))
            conexion.commit()
            if cursor.rowcount > 0:
                print('El servicio ha sido cancelado')
            else:
                 print('No se ha encontrado el servicio con el id especificado')



        def listar(conexion):
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM serviadicional')
            servicios = cursor.fetchall()
            return [servicio(*p) for p in servicios]

'''agregar_nuevo_servicio=servicio(11,'servicio de lavanderia', 15000)
agregar_nuevo_servicio.agregar_servicio(con)
'''

'''mis_servicios = servicio(15,'bar',15000)
nuevo_servicio='discoteca'
nuevo_valor=150000
mensaje = mis_servicios.actualizar_servicio(con,15, nuevo_servicio, nuevo_valor)
print(mensaje)'''

servicio_un_cancelar=servicio(id_servicio=14, tiposervicio=None, valor_servicio=None)  
servicio_un_cancelar.cancelar_servicio(con)



servicios = servicio.listar(con)
print(servicios)