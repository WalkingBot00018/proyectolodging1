import sqlite3
with sqlite3.connect('C:\\proyecto3\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db')as con:
    cursor=con.cursor()
    
    #sentencia="SELECT * FROM pagos"
    #print(cursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())
#miselect(con,'pagos','fechaemision_pago','=','23/02/2023')

def modificar(connetc,tabla,campo,dato,id_pago):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}= '{dato}' WHERE id_pago ='{id_pago}'"
    micursor.execute(sentencia)
    connetc.commit()
    print('Modificacion Exitosa')
#modificar(con,'pagos','total_pago',24000,1)    

def eliminar(connetc,tabla,campo,dato,id_pago):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}= '{dato}'"
    micursor.execute(sentencia)
    connetc.commit()
    print('Eliminicion Exitosa')
#eliminar(con,'pagos','tipocomprobante_pago','factura',10)


