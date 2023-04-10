from crudTipo_Habitaciones import *
import sqlite3
with sqlite3.connect("C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db") as c:
    cursor=c.cursor()
    class Habitaciones:
        def __init__(self,id_habitacion,numero_habitacion,tipo_habitacion,tipocamas_habitacion,descripcion_habitacion,caracteristica_habitacion,valor_habitacion,id_tipo_habitacion):
            self.id_habitacion=id_habitacion
            self.numero_habitacion=numero_habitacion
            self.tipo_habitacion=tipo_habitacion
            self.tipocamas_habitacion=tipocamas_habitacion
            self.descripcion_habitacion=descripcion_habitacion
            self.caracteristica_habitacion=caracteristica_habitacion
            self.valor_habitacion=valor_habitacion
            self.id_tipo_habitacion=id_tipo_habitacion
        
        def insert(conexion, tipo, precio, descripcion):
            cursor = conexion.cursor()
            consulta = 'INSERT INTO Habitaciones (tipo_habitacion, valor_habitacion, descripcion_habitacion) VALUES (?, ?, ?)'
            valores = (tipo, precio, descripcion)
            cursor.execute(consulta, valores)
            conexion.commit()
            
        def select(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("SELECT * from habitaciones")
            conexion.commit()

        def consultar_Habitacion(conexion,d1):
            micursor=conexion.cursor()
            sentencia=f'SELECT * FROM habitaciones WHERE id_tipo_habitacion="{d1}"'
            return (micursor.execute(sentencia).fetchall())
    
        def update(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("UPDATE habitaciones SET valor_habitacion=92000 WHERE valor_habitacion=9100",
                       (self.valor_habitacion))
            conexion.commit()
    
        def eliminar(conexion, id_habitacion):
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Habitaciones WHERE id_habitacion = ?', (id_habitacion,))
            conexion.commit()
        print('Habitación eliminada con éxito')
        #consultar_Habitacion(c,"5")

        def eliminacion_serviadicional(cls, conexion, id_servicio):
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM ServiciosAdicionales WHERE id_servicio = ?', (id_servicio,))
            conexion.commit()
        print('El servicio adicional ha sido eliminado correctamente.')

"""object=Habitaciones(2,1,"suit junior","dobles","cuarto suit con camas dobles","minibar",91000,4)
object.insert(c)
object.select(c)
object.update(c)
object.eliminar(c)
SELECT(c,"habitaciones","caracteristica_habitacion","=","Nevera y tv + aire acondicionado")
UPDATE(c,"habitaciones","caracteristica_habitacion","Nevera y tv + aire acondicionado","nevera y tv")
ELIMINAR(c,"habitaciones","id_tipo_habitacion",3)
"""
                    
    
            
            