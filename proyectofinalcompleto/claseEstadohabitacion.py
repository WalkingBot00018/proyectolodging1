from crudEstado_Habitaciones import *
import sqlite3
with sqlite3.connect("C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db") as c:
    cursor=c.cursor()
    class EHabitaciones:
        def __init__(self,id_esthab,ocupada_esthab,libre_esthab,enlimpieza_esthab,apartada_esthab):
           self.id_esthab=id_esthab
           self.ocupada_esthab=ocupada_esthab
           self.libre_esthab=libre_esthab
           self.enlimpieza_esthab=enlimpieza_esthab
           self.apartada_esthab=apartada_esthab
        
        def insert(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO estado_habitaciones VALUES()",
                           (self.ocupada_esthab,self.libre_esthab,self.enlimpieza_esthab,self.apartada_esthab))
            conexion.commit()
            
        def select(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("SELECT * from estado_habitacion")
            conexion.commit()
    
        def update(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("UPDATE estado_habitacion SET id_esthab=19 WHERE id_esthab=19",
                       (self.id_esthab))
            conexion.commit()
    
        def eliminar(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("DELETE from estado_habitacion WHERE id_esthab=19",
                       (self.id_esthab))
            conexion.commit()

object=EHabitaciones(1,"si","si","no","si")
object.insert(c)
object.select(c)
object.update(c)
object.eliminar(c)
SELECT(c,"estado_habitacion","ocupada_esthab","=","no")
UPDATE(c,"estado_habitacion","ocupada_esthab","si","no")  
ELIMINAR(c,"estado_habitacion","id_esthab",20)

           
       