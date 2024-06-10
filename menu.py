import Registrar_empleados

def menu():
    while True:
        print("Bienvenido al sistema de gestión de empleados")
        print("1. Registrar entrada de empleado")
        print("2. Registrar salida de empleado")
        print("3. Registrar nuevo empleado")
        print("4. Listar todos los empleados")
        print("5. Modificar información de un empleado")
        print("6. Despedir empleado")
        print("7. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            empleado_id = input("Ingrese el ID del empleado: ")
            Registrar_empleados.registrar_entrada_salida_empleado(empleado_id, 'entrada')
        elif opcion == "2":
            empleado_id = input("Ingrese el ID del empleado: ")
            Registrar_empleados.registrar_entrada_salida_empleado(empleado_id, 'salida')
        elif opcion == "3":
            empleado_id = input("Ingrese el ID del empleado: ")
            nombre = input("Ingrese el nombre del empleado: ")
            cargo = input("Ingrese el cargo del empleado: ")
            Registrar_empleados.registrar_empleado(empleado_id, nombre, cargo)
        elif opcion == "4":
            Registrar_empleados.listar_empleados()
        elif opcion == "5":
            empleado_id = input("Ingrese el ID del empleado a modificar: ")
            nombre = input("Ingrese el nuevo nombre del empleado (deje en blanco para mantener el actual): ")
            cargo = input("Ingrese el nuevo cargo del empleado (deje en blanco para mantener el actual): ")
            Registrar_empleados.modificar_empleado(empleado_id, nombre, cargo)
        elif opcion == "6":
            empleado_id = input("Ingrese el ID del empleado a despedir: ")
            Registrar_empleados.despedir_empleado(empleado_id)
        elif opcion == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
menu()
