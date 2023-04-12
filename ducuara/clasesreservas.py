from reserva import *
import sqlite3
from datetime import datetime


with sqlite3.connect('C:\\proyecto4\\proyectolodging1\\ducuara\\lodging2.0.db')as con:


    cursor=con.cursor()

    class reservas:
        def __init__(self, id_reservas, id_habitacion_reserva, id_usuario_reserva,tipo_reserva,fecha_reserva,fechaingre_reserva,fechasali_reserva,alojamiento_reserva,id_tipo_reserva):
            self.id_reservas = id_reservas
            self.id_habitacion_reserv = id_habitacion_reserva
            self.id_usuario_reserva = id_usuario_reserva
            self.tipo_reserva = tipo_reserva
            self.fecha_reserva = fecha_reserva
            self.fechaingre_reserva = fechaingre_reserva
            self.fechasali_reserva = fechasali_reserva
            self.alojamiento_reserva = alojamiento_reserva
            self.id_tipo_reserva = id_tipo_reserva
        
        def get_id_reserva(self):
            return self.id_reservas
            

        def verificar_disponibilidad(self,fecha_salida,fecha_ingreso):
            cursor = con.cursor()
            cursor.execute("SELECT COUNT(*) FROM reservas WHERE fechaingre_reserva <= ? AND fechasali_reserva >= ?", (fecha_salida,fecha_ingreso))
            resultado = cursor.fetchone()[0]
            return resultado > 0
        
        def set_alojamiento(self, alojamiento):
            self.alojamiento_reserva = alojamiento
        
            

        
        def listar(conexion):
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM reservas')
            reserva = cursor.fetchall()
            return [reservas(*p) for p in reserva]

reserva = reservas(12, 2, 3, 'ordinaria', '2023-04-10', '2023-04-12', '2023-04-15', 'turismo', 12)
disponible = reservas.verificar_disponibilidad(cursor, '2023-04-12', '2023-04-27')
if disponible:
    print('La habitación está disponible')
else:
    print('La habitación no está disponible')

reserva = reservas(12, 101, 1, 'ordinaria', '2023-04-01', '2023-04-15', '2023-04-20', 'Mi Hotel', 1)
print(reserva.get_id_reserva()) 


reserva = reservas(1, 101, 1, 'ordinaria', '2023-04-01', '2023-04-15', '2023-04-20', 'Mi Hotel', 1, )
print(reserva.alojamiento_reserva)  

reserva.set_alojamiento('Tu Hotel')
print(reserva.alojamiento_reserva)  


reserva = reservas.listar(con)
print(reserva)
        
    