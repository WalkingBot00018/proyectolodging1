import sqlite3
with sqlite3.connect('C:\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM pagos"
    print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())
miselect(con,'metodo_pago','efectivo_metpago','=','si')

def modificar(connetc,tabla,campo,dato,id_metpago):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_metpago ='{id_metpago}'"
    micursor.execute(sentencia)
    connetc.commit()
    print('Modificacion Exitosa')
modificar(con,'metodo_pago','tarjetacredito_metpago','si',1)    

def eliminar(connetc,tabla,campo,dato,id_metpago):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    connetc.commit()
    print('Eliminicion Exitosa')
eliminar(con,'metodo_pago','efectivo_metpago','si',1)  