from crudTipo_Habitacion import *
import sqlite3

with sqlite3.connect("C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db") as c:
    cursor=c.cursor()


class Habitacion:
    def __init__(self,id_tipo_hab,tipo_hab,hab_individual,hab_doble,hab_triple,hab_cuadruple,hab_duplex,hab_contugua,hab_site,hab_suitejunior,hab_matrimonial,id_estado_habitacion):
        self.id_tipo_hab=id_tipo_hab
        self.tipo_hab=tipo_hab
        self.hab_individual=hab_individual
        self.hab_doble=hab_doble
        self.hab_triple=hab_triple
        self.hab_cuadruple=hab_cuadruple
        self.hab_duplex=hab_duplex
        self.hab_contugua=hab_contugua
        self.hab_site=hab_site
        self.hab_suitejunior=hab_suitejunior
        self.hab_matrimonial=hab_matrimonial
        self.id_estado_habitacion=id_estado_habitacion
        
    def INSERT(self,conexion):
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO tipo_habitacion VALUES()",
                       (self.tipo_hab,self.hab_individual,self.hab_doble,self.hab_triple,self.hab_cuadruple,self.hab_duplex,self.hab_contugua,self.hab_site,self.hab_suitejunior,self.hab_matrimonial,self.id_estado_habitacion))
        conexion.commit()
    
    def SELECT(self,conexion):
        cursor=conexion.cursor()
        cursor.execute("SELECT * from tipo_habitacion")
        conexion.commit()
    
    def UPDATE(self,conexion):
        cursor=conexion.cursor()
        cursor.execute("UPDATE tipo_habitacion SET id_estado_habitacion=1 WHERE id_estado_habitacion=1",
                       (self.id_estado_habitacion))
        conexion.commit()
    
    def ELIMINAR(self,conexion):
        cursor=conexion.cursor()
        cursor.execute("DELETE FROM tipo_habitacion WHERE id_estado_habitacion=1",
                       (self.id_estado_habitacion))
        conexion.commit()

Habbitacion=Habitacion(9,"La que requiera","si","si","si","si","si","si","si","si","si",1)
Habbitacion.INSERT(c)
Habbitacion.SELECT(c)
Habbitacion.UPDATE(c)
Habbitacion.ELIMINAR(c)
UPDATE(c,"tipo_habitacion","tipo_hab","La que requiera","la que requiera")
INSERT(c,"tipo_habitacion","id_tipo_hab","tipo_hab")
ELIMINAR(c,"tipo_habitacion","id_tipo_hab",10)






    


    


       
        
        
        
    
    