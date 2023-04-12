import sqlite3
with sqlite3.connect('C:\\Ducuara1\\db\\proyectolodging\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM usuarios"
    print(micursor.execute(sentencia).fetchall())
    
def modificar(connetc,tabla,campo,dato,id_usuario):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_usuario ='{id_usuario}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')
'''modificar(con,'usuarios','nombre_usuario','saray',10) '''

def eliminar(connetc,tabla,campo,dato,id_usuario):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion Exitosa')
'''eliminar(con,'usuarios','nombre_usuario','saray',10) '''
def insertar(id_usuario,nombre_usuario,apelido_usuario,direccion_usuario,telefono_usuario,email_usuario,pass_usuario,fecharest_usuario,fechareg_usuario,id_tipo_usuario):
    micursor=con.cursor()
    sentencia=f"INSERT INTO usuarios  VALUES ({id_usuario},'{nombre_usuario}','{apelido_usuario}','{direccion_usuario}','{telefono_usuario}','{email_usuario}','{pass_usuario}','{fecharest_usuario}','{fechareg_usuario}',{id_tipo_usuario})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')

'''insertar(10,'saray','marinez','calle 8','423525','saray@gmail.com','erwef','03/05/2023','03/04/2023','10')'''

def leer():
    micursor=con.cursor()
    sentencia=f"SELECT * FROM usuarios"
    micursor.execute(sentencia)
    datos=micursor.fetchall()
    con.commit()
    print(datos)

'''leer()'''
