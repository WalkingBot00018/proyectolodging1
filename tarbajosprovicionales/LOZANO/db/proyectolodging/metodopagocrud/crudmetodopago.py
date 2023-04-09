import sqlite3
with sqlite3.connect('C:\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM metodo_pago"
    print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

#miselect(con,'metodo_pago','efectivo_metpago','=','si')

def modificar(con,tabla,campo,dato,id_metpago):
    micursor=con.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_metpago ='{id_metpago}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')

#modificar(con,'metodo_pago','tarjetacredito_metpago','si',1)

def eliminar(con,tabla,campo,dato,id_metpago):
    micursor=con.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminicion Exitosa')
#eliminar(con,'metodo_pago','efectivo_metpago','si',1)

