from crudservicios import *

class servicios:
    def __init__(self,id_pago_serv,id_servicio):
        self.id_pago=id_pago_serv
        self.id_servicio=id_servicio
    
    def consultar_servicio(self,conexion):
        print("Consultar servicio")
        Consultar=modificar(self,conexion)
        for i in Consultar:
            print(i)
    
    def agregar(self,conexion):
        print("Agregar un servicio")
        Agregar=insertar(self,conexion)
        for i in Agregar:
            print(i)
            
    