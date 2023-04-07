from tablapagos import *
import sqlite3

with sqlite3.connect('C:\\proyectolodging1\\tarbajosprovicionales\\LOZANO\\db\\proyectolodging\\lodging2.0.db') as con:
    cursor = con.cursor()

    class pago:
        def __init__(self, id_pago, id_reserva_pago, tipocomprobante_pago, numcomprobante_pago, total_pago, fechaemision_pago, fecha_pago, id_metodo_pago):
            self.id_pago = id_pago
            self.id_reserva_pago = id_reserva_pago
            self.tipocomprobante_pago = tipocomprobante_pago
            self.numcomprobante_pago = numcomprobante_pago
            self.total_pago = total_pago
            self.fechaemision_pago = fechaemision_pago
            self.fecha_pago = fecha_pago
            self.id_metodo_pago = id_metodo_pago

        def guardar(self, conexion):
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO pagos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)', 
                           (self.id_reserva_pago, self.tipocomprobante_pago, self.numcomprobante_pago, 
                            self.total_pago, self.fechaemision_pago, self.fecha_pago, self.id_metodo_pago))
            conexion.commit()

        def actualizar(self, conexion):
            cursor = conexion.cursor()
            cursor.execute('UPDATE pagos SET fechaemision_pago=?, total_pago=?, id_reserva_pago=? WHERE id_pago=?', 
                           (self.fechaemision_pago, self.total_pago, self.id_reserva_pago, self.id_pago))
            conexion.commit()

        #def eliminar(self, conexion):
            #cursor = conexion.cursor()
            #cursor.execute('DELETE FROM pagos WHERE id_pago=?', (self.id_pago,))
            #conexion.commit()

        
        
        def listar(conexion):
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM pagos')
            pagos = cursor.fetchall()
            return [pago(*p) for p in pagos]


    
    
    
    mi_pago = pago(3, 2, 'factura', '12345', 10000, '2023-04-07', '2023-04-07', 3)

    #mi_pago.guardar(con)
    #mi_pago.actualizar(con)
    #eliminar(con,'pagos','tipocomprobante_pago','factura',10)
    #modificar(con,'pagos','total_pago',24000,3) 
    #miselect(con,'pagos','fechaemision_pago','=','2023-04-07')
    pagos = pago.listar(con)
    print(pagos)


