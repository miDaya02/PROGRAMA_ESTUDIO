import Registros_campers
import Registros_trainers
import Datos_trainers_y_campers
import Estado
import Mostrar_rutas

print("**************************")
print("*   ¡BIENVENIDO A        *")
print("*    CAMPUSLANDS!        *")
print("**************************")


def menu_principal():
    Registros_campers.cargar_datos()
    while True:
        
        print("Indique su rol \n 1. Coordinador@ \n 2. Trainer \n 3. Camper \n 4. Salir")
        opcion = 0
        try:
            opcion = int(input("Indique una opción: "))
        except Exception:
            print("¡Error, valor inválido!")            
        if opcion == 1:
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
            print("¨     ¡BIENVENIDO A      ¨")
            print("¨     COORDINACIÓN!      ¨")
            print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

            print("1. Trainers \n 2.Campers \n 3. Mostrar grupos de trainers \n 4. Reportes \n 5. Para sair")
            opci = int(input("¿Qué desea realizar?: "))
            if opci == 1:
                print("==============================")
                print("=  HAS INGRESADO A TRAINERS  =")
                print("==============================")
                print("")
                print("1. Registar Trainer \n 2. Modificar Trainer")
                opc2=int(input("Indique una opción: "))
                if opc2 == 1:
                    Registros_trainers.registrar_trainer()
                    Registros_trainers.cargar_datos()
                elif opc2 ==2:
                    Registros_trainers.cargar_datos()
                    print("¿Qué desea modificar: \n 1. Horario \n 2. Area \n 3.Asignar trainer \n 4. Mostrar trainers \n 5. Para salir")
                    
                    opcc=int(input("Indique una opción: "))
                    if opcc ==1:
                        Registros_trainers.horario_trainer()
                        Registros_trainers.imprimir_trainer_info()
                        Registros_trainers.cargar_datos()
                    elif opcc ==2:
                        Registros_trainers.area_trainer()
                        Registros_trainers.imprimir_trainer_info()
                        Registros_trainers.cargar_datos()
                    elif opcc == 3:
                        Registros_trainers.grupo_del_trainer
                        Registros_trainers.imprimir_trainer_info()
                        Registros_trainers.cargar_datos()
                    elif opcc == 4:
                        Registros_trainers.imprimir_trainer_info()
                    elif opcc == 5:
                        print("")
            elif opci == 2:
                print("==============================")
                print("=  HAS INGRESADO A CAMPERS   =")
                print("==============================")
                print("")
                print("1. Registrar camper \n 2. Modificar camper")
                opcc = int(input("¿Que desea realizar?: "))
                if opcc == 1:
                    Registros_campers.registrar_camper()
                    Registros_campers.cargar_datos()
                elif opcc == 2: 
                    print("1.Estado camper \n 2. Riesgo \n 3.Ruta\n 4. Eliminar camper \n 5.Asignar grupo al camper")
                    opccm = int(input("Indique una opción: "))
                    if opccm == 1:
                        Registros_campers.imprimir_camper_info()
                        Registros_campers.estado_camper()
                        Registros_campers.cargar_datos()
                    elif opccm == 2:
                        Registros_campers.imprimir_camper_info()
                        Registros_campers.riesgo_camper()
                        Registros_campers.cargar_datos()
                    elif opccm == 3:
                        print("Rutas: \n NodaJS \n Java \n NetCore")
                        Registros_campers.ruta_camper()
                        Registros_campers.cargar_datos()
                    elif opccm == 4:
                        Registros_campers.imprimir_camper_info()
                        Registros_campers.eliminar_camper()
                        Registros_campers.cargar_datos()
                    elif opccm == 5:
                        Registros_campers.imprimir_camper_info()
                        Registros_campers.grupo_camper()
                        Registros_campers.cargar_datos()
                elif opcc == 3:
                 Estado.matricula_camper()
            elif opci == 3:
                print("Binevenido a Rutas de entrenamineto")
                print("\n1. Crear Nueva Ruta \n2. Mostrar Rutas \n3.Salir al menu Principal")
                oppc= int(input())
                if oppc == 1:
                    Mostrar_rutas.ruta_entreno()
                elif oppc == 2:
                    Mostrar_rutas.mostrar_rutas()
                elif oppc == 3:
                    print("")

            elif opci == 4 :
                print("Bienvenido a reportes")
                print("Que desea hacer ")
                print("\n1.Mostrar campers que estan Inscritos\n2.Campers que pasaron el examen inicial\n3. Entrenadores que se encuentran trabajando con CampusLands\n4. Campers que se encuentran con bajo rendimiento\n5.Campers y los trainer que se encuentren asociados a una ruta de entrenamiento\n6.Ingresar un nuevo camper graduado\n7.Mostrar campers graduados \n8.volver al menu anterior")
                opcrprte= int(input("Ingreseuna opcion"))
                if opcrprte == 1:
                    Registros_campers.imprimir_camper_info()
                elif opcrprte == 2:
                    Estado.mostrar_camper_admitidos()
                elif opcrprte == 3:
                    Registros_trainers.imprimir_trainer_info()

                    
        elif opcion == 2:
            print("1. Asignar notas a un camper \n 2.Mostrar un grupo \n 3.Salir") 
            opcion2= int(input("Escoja una opción: "))    
            if opcion2 == 1:
                Registros_campers.imprimir_camper_info()
                Registros_campers.nota_camper
                Registros_campers.cargar_datos
            elif opcion2 == 2:
                print("------------------------")
                print("-       SALIENDO       -")
                print("------------------------")

        elif opcion == 3:
            print("1. Ver trainers y Campers \n 2. Salir")
            opciones = int(input("Escoja una opción: "))
            if opciones == 1:
                if opciones == 1:
                    Datos_trainers_y_campers.imprimir_datos_trainer_camper()

print(menu_principal())