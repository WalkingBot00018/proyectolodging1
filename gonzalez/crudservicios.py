import sqlite3
with sqlite3.connect('C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM serviadicional"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_servicios):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_servicio ='{id_servicios}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')
'''modificar(con,'serviadicional','tiposervicio','wifi',3) '''

def eliminar(connetc,tabla,campo,dato,id_servicio):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion Exitosa')
'''eliminar(con,'serviadicional','tiposervicio','minibar',1)'''

def insertar(id_servicio, tiposervicio, valor_servicio):
    micursor=con.cursor()
    sentencia=f"INSERT INTO serviadicional  VALUES ({id_servicio},'{tiposervicio}',{valor_servicio})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
'''
insertar(11,'telefonia',120000)'''

def leer():
    micursor=con.cursor()
    sentencia=f"SELECT * FROM serviadicional"
    micursor.execute(sentencia)
    datos=micursor.fetchall()
    con.commit()
    print(datos)

leer()
