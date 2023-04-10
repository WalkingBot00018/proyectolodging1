import sqlite3
with sqlite3.connect('C:\\Ducuara1\\db\\proyectolodging\\lodging2_db.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM reservas"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_reservas):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_reservas ='{id_reservas}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')
'''modificar(con,'reservas','tipo_reserva','espacial',1) '''

def eliminar(connetc,tabla,campo,dato,id_reservas):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion Exitosa')
'''eliminar(con,'reservas','tipo_reserva','espacial',1)'''

def insertar(id_reservas, id_habitacion_reserva, id_usuario_reserva, tipo_reserva, fecha_reserva, fechaingre_reserva, fechasali_reserva, alojamiento_reserva, id_tipo_reserva):
    micursor=con.cursor()
    sentencia=f"INSERT INTO reservas  VALUES ({id_reservas},{id_habitacion_reserva},{id_usuario_reserva},'{tipo_reserva}','{fecha_reserva}','{fechaingre_reserva}','{fechasali_reserva}','{alojamiento_reserva}',{id_tipo_reserva})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')

'''insertar(11,5,10,'ordinaria','23/05/2023','12/09/2023','03/05/2023','turismo',12)'''

def leer():
    micursor=con.cursor()
    sentencia=f"SELECT * FROM reservas"
    micursor.execute(sentencia)
    datos=micursor.fetchall()
    con.commit()
    print(datos)

leer()

 