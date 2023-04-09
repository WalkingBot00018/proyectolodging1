import sqlite3
with sqlite3.connect("C:\\Gonzalez1\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db") as c:
    cursor=c.cursor()
    sentencia="SELECT * from habitaciones "
    print(cursor.execute(sentencia).fetchall())

def SELECT(conexion,tabla,campo,operador,dato):
    cursor=conexion.cursor()
    sentencia=f"SELECT * from {tabla} WHERE {campo} {operador}'{dato}'"
    print(sentencia)
    print(cursor.execute(sentencia).fetchall())
SELECT(c,"habitaciones","caracteristica_habitacion","=","Nevera y tv + aire acondicionado")
    

def UPDATE(connect,tabla,campo,dato,caracteristica_habitacion):
    micursor=connect.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE caracteristica_habitacion ='{caracteristica_habitacion}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Modificacion Exitosa')
UPDATE(c,"habitaciones","caracteristica_habitacion","Nevera y tv + aire acondicionado","nevera y tv")  

def ELIMINAR(connect,tabla,campo,dato):
    micursor=connect.cursor()
    sentencia=f"DELETE from {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Sin errores')
ELIMINAR(c,"habitaciones","id_tipo_habitacion",3)

    