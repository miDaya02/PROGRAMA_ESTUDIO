import json

data = {}

Archivo = "Campers.json"

def guardar_datos():
    global data
    global Archivo
    try:
        contenido = json.dumps(data, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("¡Sus datos se han guardado exitosamente!")
    except Exception:
        print("¡Error, no se han podido guardar sus datos!")

def cargar_datos():
    global data
    global Archivo
    try:
        with open(Archivo, "r") as file:
            data = json.load(file)
        print("¡Sus datos se han guardado exitosamente!")
    except Exception:
        print("¡Error, no se han podido guardar sus datos!")

def registrar_camper():
    global data 
    doc = int( input("Indique el documento del camper: "))
    camper = {}
    camper["Nombre"] = input("Nombre del camper: ")
    camper["apellido"] = input("Apellidos del camper: ")
    camper["direccion"] = input("Dirección del camper: ")
    camper["acudiente"] = input("Datos del acudiente del camper: ")
    try:
        camper["telefono"] = int(input("Número de telefono: "))
    except ValueError:
        print("¡Error, valor inválido")
        return
    camper["Estado"] = ("")
    camper["Riesgo"] = ("")
    camper["Ruta"] = ("")
    camper["Nota"] = ("")
    camper["Grupo"] = ("")
    data[doc] = camper
    
    guardar_datos()

def estado_camper():
    global data
    doc = input("Indique el documento del camper: ")
    if doc in data:
        estado_del_camper = input("Ingrese el estado nuevo: ")
        data[doc]["estado"] = estado_del_camper
        print("Estado actualizado")
        guardar_datos()
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")
        
def riesgo_camper():
    global data
    doc = input("Ingrese el documento del camper: ")
    if doc in data:
        riesgocamper = input("Ingrese riesgo: ")
        data[doc]["riesgo"] = riesgocamper
        print("Riesgo actualizado")
        guardar_datos()
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")
        
def ruta_camper():
    global data
    doc = input("Ingrese el documento del camper: ")
    if doc in data:
        rutacamper = input("Ingrese la ruta: ")
        data[doc]["ruta"] = rutacamper
        print("Ruta asignada")
        guardar_datos()
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")

def nota_camper():
    global data
    doc = input("Ingrese el documento del camper: ")
    if doc in data:
        nota1 = float(input("Ingrese la primera nota (60%): "))
        porcentaje1 = 60

        nota2 = float(input("Ingrese la segunda nota (30%): "))
        porcentaje2 = 30

        nota3 = float(input("Ingrese la tercera nota (10%): "))
        porcentaje3 = 10

        if not isinstance(nota1, (int, float)) or not isinstance(nota2, (int, float)) or not isinstance(nota3, (int, float)):
            print("Las notas deben ser valores numéricos.")
            return

        if porcentaje1 + porcentaje2 + porcentaje3 != 100:
            print("Los porcentajes deben sumar 100%.")
            return

        nota_final = (nota1 * porcentaje1 / 100) + (nota2 * porcentaje2 / 100) + (nota3 * porcentaje3 / 100)

        data[doc]["nota"] = nota_final
        guardar_datos()
        print(f"La nota final del camper es: {nota_final}")
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")
        
        
def eliminar_camper():
    global data
    doc = input("Ingrese el documento del camper: ")
    if doc in data:
        del data[doc]
        print("Se ha eliminado el camper")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")


def grupo_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el grupo: ")
    if doc in data:
        campero = input("Ingrese el grupo al que sera asignado: ")
        data[doc]["grupo"] = campero
        print("Se ha asignado el grupo")
        guardar_datos()
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")

def ver_notas_camper():
    global data
    doc = input("Ingrese el documento del camper: ")
    if doc in data:
        camper = data[doc]
        Nombre = camper.get("Nombre", "")
        Apellido = camper.get("apellido", "")
        nota = data[doc].get("Nota", "No hay notas registradas para este camper.")
        print(f"ombre: {Nombre} {Apellido} , Nota del camper:", nota)
    else:
        print("¡Error, No se encuentra ningun camper registrado con ese documento!")

def imprimir_camper_info():
    global data
    print("Información de todos los Campers:\n")
    for doc, camper in data.items():
        nombre = camper.get("Nombre", "")
        apellido = camper.get("apellido", "")
        if nombre and apellido:
            print(f"Documento: {doc}, Nombre: {nombre} {apellido}")
        else:
            print(f"No se encontró información completa para el camper con documento {doc}.")