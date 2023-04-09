import sqlite3
with sqlite3.connect("C:\\Gonzalez1\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db") as c:
    cursor=c.cursor()
    sentencia="SELECT * FROM tipo_habitacion "
    print(cursor.execute(sentencia).fetchall())
    
def UPDATE(connect,tabla,campo,dato,tipo_hab):
    micursor=connect.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE tipo_hab ='{tipo_hab}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Modificacion Exitosa')
UPDATE(c,"tipo_habitacion","tipo_hab","La que requiera","la que requiera")  

def INSERT(connect,tabla):
    cursor=connect.cursor()
    sentencia=f"INSERT INTO {tabla} VALUES(15,'hola') "
    cursor.execute(sentencia)
    connect.commit()
    print("Modificacion exitosa")
INSERT(c,"tipo_habitacion","id_tipo_hab","tipo_hab")

def ELIMINAR(connect,tabla,campo,dato):
    micursor=connect.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    connect.commit()
    print('Sin errores')
ELIMINAR(c,"tipo_habitacion","id_tipo_hab",10)

    