import sqlite3
with sqlite3.connect('C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM usuarios"
    print(micursor.execute(sentencia).fetchall())


def seleccionar_usuario(con):
    micursor=con.cursor()
    select=f'SELECT * FROM usuarios'
    print(' resultado: \n')
    return (micursor.execute(select).fetchall())
#Ejemplo
#selectAll_tbUsuario(database)
    
def modificar(connectc,tabla,campo,dato,id_usuario):
    micursor=connectc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_usuario ='{id_usuario}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion Exitosa')
#modificar(con,'usuarios','nombre_usuario','saray',2) 

def eliminar_usuario(connetc,tabla,campo,dato,id_usuario):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion Exitosa')
'''eliminar(con,'usuarios','nombre_usuario','saray',10) '''
def insertar_USUARIO(con,id_usuario,nombre_usuario,apelido_usuario,direccion_usuario,telefono_usuario,email_usuario,pass_usuario,fecharest_usuario,fechareg_usuario,id_tipo_usuario):
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
def conusuario(conexion,condition):
            micursor=conexion.cursor()
            sentencia=f'SELECT * FROM usuarios WHERE id_usuarios="{condition}"'
            print(' resultado: \n')
            return (micursor.execute(sentencia).fetchall())
#Ejemplo
#conusuario('id_Tipo_usuario',2)
