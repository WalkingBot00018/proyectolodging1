from crudusuarios import *
import sqlite3

with sqlite3.connect('C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')as con:
    cursor=con.cursor()

    class usuario:
        def __init__(self, id_usuario, nombre_usuario, apellido_usuario, direccion_usuario, telefono_usuario, email_usuario, pass_usuario, fecharest_usuario, fechareg_usuario, id_tipo_usuario):
            self.id_usuario = id_usuario
            self.nombre_usuario = nombre_usuario
            self.apellido_usuario = apellido_usuario
            self.direccion_usuario = direccion_usuario
            self.telefono_usuario = telefono_usuario
            self.email_usuario = email_usuario
            self.pass_usuario = pass_usuario
            self.fecharest_usuario =  fecharest_usuario
            self.fechareg_usuario = fechareg_usuario
            self.id_tipo_usuario = id_tipo_usuario


        def buscar_por_id(id_usuario):
            cursor = con.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario=?", (id_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado
            else:
                return None
            

        def cambiar_contraseña(self, nueva_contraseña):
            cursor = con.cursor()
            datos = (nueva_contraseña, self.id_usuario)
            cursor.execute("UPDATE usuarios SET pass_usuario=? WHERE id_usuario=?", datos)
            con.commit()
            

        def listar(conexion):
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            return[usuario(*p) for p in usuarios]
        
        def conusuario(conexion,condition,id_usuario):
            conexion = sqlite3.connect('C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')
            micursor = conexion.cursor()
            sentencia=f'SELECT * FROM usuarios WHERE id_usuarios=?', (id_usuario)
            print(' resultado: \n')
            'micursor.execute(sentencia, (condition,)).fetchall()'
#Ejemplo
        conusuario(con,'id_Tipo_usuario',2)
            
usuario_buscado = usuario(*usuario.buscar_por_id(id_usuario=4))


if usuario_buscado is not None:
    print("Usuario encontrado:")
    print("ID:", usuario_buscado.id_usuario)
    print("Nombre:", usuario_buscado.nombre_usuario)
    print("Apellido:", usuario_buscado.apellido_usuario)
    print("Dirección:", usuario_buscado.direccion_usuario)
    print("Teléfono:", usuario_buscado.telefono_usuario)
    print("Email:", usuario_buscado.email_usuario)
    print("Contraseña:", usuario_buscado.pass_usuario)
    print("Fecha de registro:", usuario_buscado.fechareg_usuario)
    print("Fecha de última reserva:", usuario_buscado.fecharest_usuario)
    print("Tipo de usuario:", usuario_buscado.id_tipo_usuario)
else:
    print("No se encontró ningún usuario con el ID especificado.")


usuario_actual = usuario(*usuario.buscar_por_id(3))
usuario_actual.cambiar_contraseña('nueva_contraseña')



usuarios = usuario.listar(con)
print(usuarios)


        


