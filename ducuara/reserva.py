import sqlite3
with sqlite3.connect('C:\\Ducuara1\\db\\proyectolodging\\lodging2_db.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM reservas"
    print(micursor.execute(sentencia).fetchall())

def modificar_reserva(connetc,val2,d1,c1):
    micursor=connetc.cursor()
    sentencia=f"UPDATE reservas SET {val2}= '{d1}' WHERE id_reservas ='{c1}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')
'''modificar(con,'reservas','tipo_reserva','espacial',1) '''

def eliminar_reserva(connetc,d1):
    micursor=connetc.cursor()
    sentencia=f'DELETE FROM reservas WHERE id_reservas= "{d1}"'
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion Exitosa')
'''eliminar(con,'reservas','tipo_reserva','espacial',1)'''

def insertar_reserva(id_reservas, id_habitacion_reserva, id_usuario_reserva, tipo_reserva, fecha_reserva, fechaingre_reserva, fechasali_reserva, alojamiento_reserva, id_tipo_reserva):
    micursor=con.cursor()
    sentencia=f"INSERT INTO reservas  VALUES ({id_reservas},{id_habitacion_reserva},{id_usuario_reserva},'{tipo_reserva}','{fecha_reserva}','{fechaingre_reserva}','{fechasali_reserva}','{alojamiento_reserva}','{id_tipo_reserva}')"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')

'''insertar(11,5,10,'ordinaria','23/05/2023','12/09/2023','03/05/2023','turismo',12)'''

def consultarReservaUsuario(connetc,d1):
    micursor=connetc.cursor()
    sentencia=f'SELECT * FROM reservas WHERE id_usuario_reserva="{d1}"'
    return (micursor.execute(sentencia).fetchall())
'''consultarReservaUsuario(con,8)'''

def consultarReservar(conexion,d1):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM reservas WHERE id_reservas="{d1}"'
    return (micursor.execute(sentencia).fetchall())





def leer():
    micursor=con.cursor()
    sentencia=f"SELECT * FROM reservas"
    micursor.execute(sentencia)
    datos=micursor.fetchall()
    con.commit()
    print(datos)

'''leer()'''

 