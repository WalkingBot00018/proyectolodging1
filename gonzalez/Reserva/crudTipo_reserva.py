import sqlite3
with sqlite3.connect("C:\\Gonzalez1\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db") as c:
    cursor=c.cursor()
    sentencia="SELECT * FROM reservas"
    print(cursor.execute(sentencia).fetchall())

def INSERTR(conexion,r1,r2,r3,r4,r5,r6,r7,r8):
    micursor=conexion.cursor()
    sentencia=f'INSERT INTO reservas(id_habitacion_reserva,id_usuario_reserva,tipo_reserva,fecha_reserva,fechaingre_reserva,fechasali_reserva,alojamiento_reserva,id_tipo_reserva) VALUES ("{r1}","{r2}","{r3}","{r4}","{r5}","{r6}","{r7}","{r8}")'
    micursor.execute(sentencia)
    conexion.commit()
    print("Se agrego una nueva reserva")
INSERTR(c,"id_habitacion_reserva","id_usuario_reserva","tipo_reserva","fecha_reserva","fechaingre_reserva","fechasali_reserva","alojamiento_reserva","id_tipo_reserva",8,5,"especial","2023-01-09","2023-01-09","2023-01-15","negocios",15)

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

    