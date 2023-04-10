from crudTipo_reserva import *
import sqlite3
with sqlite3.connect("C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db")as c:
    cursor=c.cursor()
    class Reserva:
        def __init__(self,id_reserva,id_habitacion_reserva,id_usuario_reserva,tipo_reserva,fecha_reserva,fechaingre_reserva,fechasali_reserva,alojamiento_reserva,id_tipo_reserva):
            self.id_reserva=id_reserva
            self.id_habitacion_reserva=id_habitacion_reserva
            self.id_usuario_reserva=id_usuario_reserva
            self.tipo_reserva=tipo_reserva
            self.fecha_reserva=fecha_reserva
            self.fechaingre_reserva=fechaingre_reserva
            self.fechasali_reserva=fechasali_reserva
            self.alojamiento_reserva=alojamiento_reserva
            self.id_tipo_reserva=id_tipo_reserva
        
        def INSERT(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO reservas VALUES()",
                       (self.tipo_reserva,self.fecha_reserva,self.fechaingre_reserva,self.fechasali_reserva,self.alojamiento_reserva,self.id_tipo_reserva))
            conexion.commit()
    
        def SELECT(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("SELECT * from reservas")
            conexion.commit()
    
        def UPDATE(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("UPDATE reservas SET tipo_reserva=Legal WHERE tipo_reserva=legal",
                       (self.tipo_reserva))
            conexion.commit()
    
        def ELIMINAR(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM reservas WHERE id_tipo_reserva=10",
                       (self.id_tipo_reserva))
            conexion.commit()

ob=Reserva(1,1,1,"Legal","22/03/2023","02/01/2023","30/03/2023","negocios",10)
ob.INSERT(c)
ob.SELECT(c)
ob.UPDATE(c)
ob.ELIMINAR(c)
SELECT(c,"reservas","tipo_reserva","=","ordinaria")
UPDATE(c,'reservas','tipo_reserva',"Especial","especial")  
ELIMINAR(c,'reservas','alojamiento_reserva',"estadia")

                    
    