from crudmetodopago import *
import sqlite3

with sqlite3.connect('C:\\proyecto4\\proyectolodging1\\proyectofinalcompleto\\lodging2.0.db') as con:
    cursor = con.cursor()

    class metodo_pago:
        def __init__(self, id_metpago, efectivo_metpago, tarjetacredito_metpago, tarjetavirtual_metpago, transferenciabancaria_metpago):
            self.id_metpago = id_metpago
            self.efectivo_metpago = efectivo_metpago
            self.tarjetacredito_metpago = tarjetacredito_metpago
            self.tarjetavirtual_metpago = tarjetavirtual_metpago
            self.transferenciabancaria_metpago = transferenciabancaria_metpago
            
    
        
        def crear_metodo_pago(cls, conexion, efectivo, tarjeta_credito, tarjeta_virtual, transferencia_bancaria):
        
            micursor = conexion.cursor()
            micursor.execute('INSERT INTO metodo_pago (efectivo_metpago, tarjetacredito_metpago, tarjetavirtual_metpago, transferenciabancaria_metpago) VALUES (?, ?, ?, ?)',
                        (efectivo, tarjeta_credito, tarjeta_virtual, transferencia_bancaria))
            id_metpago = micursor.lastrowid
            conexion.commit()
        
            return cls(id_metpago, efectivo, tarjeta_credito, tarjeta_virtual, transferencia_bancaria)
        
    
        
        def leer_metodo_pago(cls, conexion, id_metpago):
            micursor = conexion.cursor()
            micursor.execute('SELECT * FROM metodo_pago WHERE id_metpago = ?', (id_metpago,))
            resultado = micursor.fetchone()
            if resultado:
                return cls(*resultado)
            else:
                return None
        
        def actualizar_metodo_pago(self,conexion):
        
            micursor = conexion.cursor()
            micursor.execute('UPDATE metodo_pago SET efectivo_metpago = ?, tarjetacredito_metpago = ?, tarjetavirtual_metpago = ?, transferenciabancaria_metpago = ? WHERE id_metpago = ?',
                        (self.efectivo_metpago, self.tarjetacredito_metpago, self.tarjetavirtual_metpago, self.transferenciabancaria_metpago, self.id_metpago))
            conexion.commit()
        
        
        def eliminar_metodo_pago(self,conexion):
        
            micursor = conexion.cursor()
            micursor.execute('DELETE FROM metodo_pago WHERE id_metpago = ?', (self.id_metpago,))
            conexion.commit()

        def guardar(self, conexion):
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO metodo_pago VALUES (NULL, ?, ?, ?, ?)', 
                           (self.efectivo_metpago, self.tarjetacredito_metpago, self.tarjetavirtual_metpago, self.transferenciabancaria_metpago))
            conexion.commit()

       
    
        # Crea una instancia de la clase metodo_pago
    #metodo_pago1 = metodo_pago.crear_metodo_pago(con, True, False, True, False)

    # Recuperar una instancia existente de la clase metodo_pago de la base de datos
    #metodo_pago_leido = metodo_pago.leer_metodo_pago(con, 7)
    #actmetpago= metodo_pago(8,'si', 'no', 'si', 'no')
    #actmetpago.guardar(con)

    # Actualizar la instancia de la clase metodo_pago
    """
    metodo_pago_leido.efectivo_metpago = False
    actmetpago.actualizar_metodo_pago(con)"""

    # Eliminar la instancia de la clase metodo_pago
    #metodo_pago_leido.eliminar_metodo_pago(con)
    
    #miselect(con,'metodo_pago','efectivo_metpago','=','si')
    #modificar(con,'metodo_pago','tarjetacredito_metpago','si',10)
    #eliminar(con,'metodo_pago','efectivo_metpago','si',1)
    
    
