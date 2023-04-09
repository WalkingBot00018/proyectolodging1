import sqlite3
with sqlite3.connect("C:\\Gonzalez1\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db") as c:
    cursor=c.cursor()
    sentencia="SELECT * from estado_habitacion "
    print(cursor.execute(sentencia).fetchall())

def SELECT(conexion,tabla,campo,operador,dato):
    cursor=conexion.cursor()
    sentencia=f"SELECT * from {tabla} WHERE {campo} {operador}'{dato}'"
    print(sentencia)
    print(cursor.execute(sentencia).fetchall())
SELECT(c,"estado_habitacion","ocupada_esthab","=","no")
    

def UPDATE(connect,tabla,campo,dato,ocupada_esthab):
    micursor=connect.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE ocupada_esthab ='{ocupada_esthab}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Modificacion Exitosa')
UPDATE(c,"estado_habitacion","ocupada_esthab","si","no")  

def ELIMINAR(connect,tabla,campo,dato):
    micursor=connect.cursor()
    sentencia=f"DELETE from {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Sin errores')
ELIMINAR(c,"estado_habitacion","id_esthab",20)