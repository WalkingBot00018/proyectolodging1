from clasespagos import *


def menu():
    opcion = None
    while opcion != '0':
        print('------ Menú Principal ------')
        print('1. actualizar pagos')
        print('2. guardar pago')
        print('3. Buscar pagos por fecha')
        print('4. buscar pagos en lista')
        print('5. eliminar pago')
        print('6. modificar pago')
        print('7 seleccionar pago')
        print('0. Salir')
        opcion = input('Selecciona una opción: ')
        
        if opcion == '1':
            pago.actualizar(conexion)
        elif opcion == '2':
            pago.guardar(con)
        elif opcion == '3':
           pago.buscar_por_fecha(con)
        elif opcion == '4':
           pago.listar(conexion)
        elif opcion == '5':
            eliminar()
        elif opcion == '6':
            modificar()
        elif opcion =='7':
            miselect()
        elif opcion == '0':
            print('Saliendo del programa...')
        else:
            print('Opción no válida. Inténtalo de nuevo.')
            
if __name__ == '__main__':
    menu()
