import Registros_campers
import Registros_trainers
import Datos_trainers_y_campers

print("**************************")
print("*   ¡BIENVENIDO A        *")
print("*    CAMPUSLANDS!        *")
print("**************************")


def menu_principal():
    Registros_campers.cargar_datos()
    while True:
        
        print("Indique su rol \n 1. Coordinador@ \n 2. Trainer")
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

            print("1. Trainers \n 2.Campers \n 3. Mostrar grupos de trainers")
            opci=int(input("¿Qué desea realizar?: "))
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
                    print("¿Qué desea modificar: \n 1. Horario \n 2. Area \n 3.Asignar trainer")
                    
                    opctm=int(input("Indique una opción: "))
                    if opcc ==1:
                        Registros_trainers.horario_del_trainer()
                        Registros_trainers.cargar_datos()
                    elif opcc ==2:
                        Registros_trainers.cargar_datos()
                        Registros_trainers.area_del_trainer()
                    elif opcc == 3:
                        Registros_trainers.cargar_datos()
                        Registros_trainers.grupo_del_trainer()
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
                        Registros_campers.cargar_datos()
                        Registros_campers.estado_camper()
                    elif opccm == 2:
                        Registros_campers.cargar_datos()
                        Registros_campers.riesgo_camper()
                    elif opccm == 3:
                        print("Rutas: \n NodaJS \n Java \n NetCore")
                        Registros_campers.cargar_datos()
                        Registros_campers.ruta_camper()
                    elif opccm == 4:
                        Registros_campers.cargar_datos()
                        Registros_campers.eliminar_camper()
                    elif opccm == 5:
                        Registros_campers.cargar_datos()
                        Registros_campers.grupo_camper()
                    
        elif opcion == 2:
            print("1. Asignar notas a un camper \n 2.Salir") 
            opcion2= int(input("Escoja una opción: "))    
            if opcion2 == 1:
                Registros_campers.cargar_datos
                Registros_campers.nota_camper
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