from Tipo_Habitaciones import *
import sqlite3
with sqlite3.connect("C:\\Gonzalez1\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db") as c:
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
        
        def insert(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO habitaciones VALUES()",
                           (self.numero_habitacion,self.tipo_habitacion,self.tipocamas_habitacion,self.descripcion_habitacion,self.caracteristica_habitacion,self.valor_habitacion,self.id_tipo_habitacion))
            conexion.commit()
            
        def select(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("SELECT * from habitaciones")
            conexion.commit()
    
        def update(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("UPDATE habitaciones SET valor_habitacion=92000 WHERE valor_habitacion=9100",
                       (self.valor_habitacion))
            conexion.commit()
    
        def eliminar(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("DELETE from habitaciones WHERE id_tipo_habitacion=6",
                       (self.id_tipo_habitacion))
            conexion.commit()

object=Habitaciones(2,1,"suit junior","dobles","cuarto suit con camas dobles","minibar",91000,4)
object.insert(c)
object.select(c)
object.update(c)
object.eliminar(c)
SELECT(c,"habitaciones","caracteristica_habitacion","=","Nevera y tv + aire acondicionado")
UPDATE(c,"habitaciones","caracteristica_habitacion","Nevera y tv + aire acondicionado","nevera y tv")
ELIMINAR(c,"habitaciones","id_tipo_habitacion",3)

                    
    
            
            