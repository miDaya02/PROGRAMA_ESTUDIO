import json
data = []

Archivo= "Estado.json"

def guardar_datos():
    global data
    global Archivo
    try:
        contenido = json.dumps(data, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("¡Sus datos se han guardado correctamente!")
    except Exception:
        print("¡Error al guardar datos!")

def cargar_datos():
    global data
    global Archivo
    try:
        with open(Archivo, "r") as file:
            data = json.load(file)
        print("¡Sus datos se han guardado correctamente!!")
    except Exception:
        print("Error al cargar datos")