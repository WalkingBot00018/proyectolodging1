from crudTipo_usuario import *
import sqlite3
with sqlite3.connect("C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db")as c:
    cursor=c.cursor()
    class Tusuario:
        def __init__(self,tipo_usuario,tipo):
            self.tipo_usuario=tipo_usuario
            self.tipo=tipo
        
        def INSERT(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO reservas VALUES()",
                       (self.tipo_usuario,self.tipo))
            conexion.commit()
    
        def SELECT(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("SELECT * from tipo_usuario")
            conexion.commit()
    
        def UPDATE(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("UPDATE tipo_usuario SET tipo=5 WHERE tipo_reserva=8",
                       (self.tipo_usuario))
            conexion.commit()
    
        def ELIMINAR(self,conexion):
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM tipo_usuario WHERE tipo=3",
                       (self.tipo))
            conexion.commit()

ob=Tusuario(1,2)
ob.INSERT(c)
ob.SELECT(c)
ob.UPDATE(c)
ob.ELIMINAR(c)
SELECT(c,"tipo_usuario","tipo","=","2")
UPDATE(c,'tipo_usuario','tipo_usuario',"0","2")    
ELIMINAR(c,'tipo_usuario','tipo',"5")
