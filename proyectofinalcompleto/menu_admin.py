from admin import *
while True:
    print("\nBienvenido a la aplicación de Administrador. ¿Qué acción deseas realizar?\n")
    print("1. Consultar habitaciones disponibles")
    print("2. Agregar habitación")
    print("3. Actualizar habitación")
    print("4. Eliminar habitación")
    print("5. Consultar servicios adicionales")
    print("6. Crear servicio adicional")
    print("7. Actualizar servicio adicional")
    print("8. Eliminar servicio adicional")
    print("9. Consultar usuarios")
    print("10. Crear usuario")
    print("11. Salir de la aplicación\n")
    
    opcion = input("Ingresa el número de la acción que deseas realizar: ")

    if opcion == "1":
        n2.consultar_Habitacion(con, d1)
    elif opcion == "2":
        n2.agregarHabitacion(con)
    elif opcion == "3":
        n2.actualizarHabitacion(con)
    elif opcion == "4":
        n2.eliminarHabitacion(con)
    elif opcion == "5":
        n2.consultarServicios(con)
    elif opcion == "6":
        n2.crear_Serviadicional(con)
    elif opcion == "7":
       n2.actualizar_servicio(con)
    elif opcion == "8":
        n2.elimiar_servicios(con)
    elif opcion == "9":
        n2.consulta_de_empleados(con)
    elif opcion == "10":
        n2.crear_usuarios(con)
    elif opcion == "11":
        print("\n¡Gracias por utilizar nuestra aplicación! ¡Hasta luego!")
        break
    else:
        print("\n¡Opción inválida! Ingresa un número del 1 al 11.")
