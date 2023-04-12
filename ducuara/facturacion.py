import sqlite3
with sqlite3.connect('C:\\Ducuara1\\db\\proyectolodging\\lodging2.0.db')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM facturacion"
    print(micursor.execute(sentencia).fetchall())

def insertar_factura(connetc,d1,d2,d3,d4):
    micursor=connetc.cursor()
    sentencia=f'INSERT INTO facturacion (Id_fa,Fecha_fa,Id_usu,ValorTotal_fa) VALUES ("{d1}","{d2}","{d3}","{d4}")'
    micursor.execute(sentencia)
    con.commit()
'''print('La insercion del dato fue insertado')'''

'''insertar_factura(con,'1','2024-04-07','595950','2000000')'''

def consultar_factura(connetc):
    micursor=connetc.cursor()
    sentencia=f'SELECT * FROM facturacion'
    print(micursor.execute(sentencia).fetchall())

'''consultar_factura(con)'''

def consultar_usuario(connetc,d1):
    micursor=connetc.cursor()
    sentencia=f'SELECT * FROM facturacion WHERE Id_usu="{d1}"'
    print(micursor.execute(sentencia).fetchall())

'''consultar_usuario(con,1584)'''

def actualizar_factura(connetc,d1,c1):
    micursor=connetc.cursor()
    sentencia=f'UPDATE facturacion SET ValorTotal_fa="{d1}" WHERE Id_fa="{c1}"'
    micursor.execute(sentencia)
    connetc.commit()
    print('Registro actualizado correctamente')

'''actualizar_factura(con,12000,2)'''

def eliminar_factura(connetc,d1):
    micursor=connetc.cursor()
    sentencia=f'DELETE FROM facturacion WHERE id_fa="{d1}"'
    micursor.execute(sentencia)
    connetc.commit()
    print('Registro eliminado corretamente')

'''eliminar_factura(con,1)'''

