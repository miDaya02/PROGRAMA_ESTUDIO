import json

data = {}

Archivo = "Trainer.json"

def guardar_datos():
    global data
    global Archivo
    try:
        contenido = json.dumps(data, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos():
    global Archivo
    try:
        with open(Archivo, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente!!")
    except Exception:
        print("Error al cargar datos")

def registrar_trainer():
    global data
    doc = int( input("Documento del trainer: "))
    trainer = {}
    trainer["Nombre"] = input("Nombre del trainer: ")
    trainer["Apellidos"] = input("Apellidos del trainer: ")
    trainer["Direccion"] = input("Dirección del trainer: ")
    try:
        trainer["Telefono"] = int(input("Número de telefono: "))
    except ValueError:
        print("¡Error, ingrese un valor válido!")
        return
    trainer["Horario"] = ("")
    trainer["Area"] = ("")
    trainer["Grupo trainer"] = ("")
    data[doc] = trainer
    
    guardar_datos()
    
def horario_trainer():
    global data
    doc = input("Documento del trainer : ")
    if doc in data:
        estado_del_camper = input("Horario del trainer: ")
        data[doc]["Horario"] = estado_del_camper
        print("Horario nuevo")
        guardar_datos()
    else:
        print("No se ha registrado ningun trainer con ese documento")
        
def area_trainer():
    global data
    doc = input("Documento del trainer : ")
    if doc in data:
        areatrainer = input("Area del trainer: ")
        data[doc]["Area del trainer"] = areatrainer
        print("Area nueva del trainer")
        guardar_datos()
    else:
        print("No se ha registrado ningun trainer con ese documento")

def grupo_del_trainer():
    global data
    doc = input("Documento del trainer : ")
    if doc in data:
        grupotrainer = input("Grupo del trainer: ")
        data[doc]["Area del trainer"] = grupotrainer
        print("Area del trainer actualizada")
        guardar_datos()
    else:
        print("No se ha registrado ningun trainer con ese documento")
    
def imprimir_trainer_info():
    global data
    print("Información de todos los Trainers:\n")
    for doc, trainer in data.items():
        nombre = trainer.get("Nombre", "")
        apellidos = trainer.get("Apellidos", "")
        if nombre and apellidos:
            print(f"Documento: {doc}, Nombre: {nombre} {apellidos}")
        else:
            print(f"No se encontró información completa para el trainer con documento {doc}.")
