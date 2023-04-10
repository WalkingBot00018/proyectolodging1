import sqlite3
with sqlite3.connect("C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db") as c:
    cursor=c.cursor()
    sentencia="SELECT * FROM reservas"
    print(cursor.execute(sentencia).fetchall())

def SELECT(conexion,tabla,campo,operador,dato):
    cursor=conexion.cursor()
    sentencia=f"SELECT FROM {tabla} WHERE {campo} {operador}'{dato}'"
    print(sentencia)
    print(cursor.execute(sentencia).fetchall())
SELECT(c,"reservas","tipo_reserva","=","ordinaria")
    
def UPDATE(connect,tabla,campo,dato,tipo_reserva):
    cursor=connect.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE tipo_reserva ='{tipo_reserva}'"
    cursor.execute(sentencia)
    connect.commit()
    print('Modificacion Exitosa')
UPDATE(c,'reservas','tipo_reserva',"Especial","especial")  

def ELIMINAR(connect,tabla,campo,dato):
    cursor=connect.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    cursor.execute(sentencia)
    connect.commit()
    print('Sin errores')
ELIMINAR(c,'reservas','alojamiento_reserva',"estadia")

    