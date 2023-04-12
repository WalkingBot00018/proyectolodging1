import sqlite3

with sqlite3.connect('C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.dbC:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db') as proyecto:
    micursor=proyecto.cursor()

    def Insert_Serviadicionales(conexion,tiposervicio,valorservicio):
        micursor=conexion.cursor()
        sentecia=f'INSERT INTO serviadicional (TipoServicio,valor_servicio)  VALUES ("{tiposervicio}", "{valorservicio}")'
        micursor.execute(sentecia)
        proyecto.commit()
        print('El registro se agrego con exito')
    
    Insert_Serviadicionales(proyecto,'sAdi',3)
    
    def select_Serviadicionales(conexion):
        micursor=conexion.cursor()
        sentencia=f'SELECT * FROM serviadicional'
        return (micursor.execute(sentencia).fetchall())
    
    print(select_Serviadicionales(proyecto))
    
    def select_serviadicional_condicion(conexion,id):
        micursor=conexion.cursor()
        sentencia=f'SELECT * FROM serviadicional WHERE id_servicio="{id}"'
        return (micursor.execute(sentencia).fetchall())
    
    print(select_serviadicional_condicion(proyecto,1))
    
    def modificacion_serviadicional(conexion,campo,dato,id):
        micursor=conexion.cursor()
        sentencia=f"UPDATE serviadicional SET {campo}='{dato}' WHERE id_servicio='{id}'"
        micursor.execute(sentencia)
        proyecto.commit()
        print('Modificación con exito.')
    
    modificacion_serviadicional(proyecto,'TipoServicio','servicio adicional',1)
    
    def eliminacion_serviadicional(conexion,id):
        micursor=conexion.cursor()
        sentecia=f'DELETE FROM serviadicional WHERE id_servicio="{id}"'
        micursor.execute(sentecia)
        proyecto.commit()
        print('Eliminación exitosa.')
    
    eliminacion_serviadicional(proyecto,1)
