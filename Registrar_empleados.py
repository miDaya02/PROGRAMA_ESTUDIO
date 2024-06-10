import json
import csv
from datetime import datetime

def listar_empleados():
    try:
        with open('empleados.json', 'r') as f:
            empleados = json.load(f)
            if empleados:
                print("Lista de empleados:")
                for empleado_id, info in empleados.items():
                    print(f"ID: {empleado_id}, Nombre: {info['nombre']}, Cargo: {info['cargo']}")
            else:
                print("No hay empleados registrados.")
    except FileNotFoundError:
        print("No hay empleados registrados.")

def modificar_empleado(empleado_id, nombre=None, cargo=None):
    try:
        with open('empleados.json', 'r') as f:
            empleados = json.load(f)
    except FileNotFoundError:
        print("No hay empleados registrados.")
        return
    
    if empleado_id not in empleados:
        print("Error: El empleado no existe.")
        return
    
    empleado = empleados[empleado_id]
    if nombre:
        empleado['nombre'] = nombre
    if cargo:
        empleado['cargo'] = cargo
    
    with open('empleados.json', 'w') as f:
        json.dump(empleados, f, indent=4)
    
    print("Empleado modificado exitosamente.")

def despedir_empleado(empleado_id):
    try:
        with open('empleados.json', 'r') as f:
            empleados = json.load(f)
    except FileNotFoundError:
        print("No hay empleados registrados.")
        return
    
    if empleado_id not in empleados:
        print("Error: El empleado no existe.")
        return
    
    empleado = empleados[empleado_id]
    empleado['estado'] = 'despedido'
    
    with open('empleados.json', 'w') as f:
        json.dump(empleados, f, indent=4)
    
    print("Empleado despedido exitosamente.")


def registrar_empleado(empleado_id, nombre, cargo):
    # Cargar los datos de empleados desde el archivo JSON
    try:
        with open('empleados.json', 'r') as f:
            empleados = json.load(f)
    except FileNotFoundError:
        empleados = {}

    # Verificar si el empleado ya existe
    if empleado_id in empleados:
        print("Error: El empleado ya está registrado.")
        return

    # Crear un nuevo registro de empleado
    nuevo_empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "hora_entrada": "",
        "hora_salida": "",
        "advertencia": ""
    }

    # Agregar el nuevo empleado al diccionario de empleados
    empleados[empleado_id] = nuevo_empleado

    # Guardar los datos actualizados en el archivo JSON
    with open('empleados.json', 'w') as f:
        json.dump(empleados, f, indent=4)

    print("Empleado registrado exitosamente.")


def registrar_entrada_salida_empleado(empleado_id, accion):
    # Cargar los datos de empleados desde el archivo JSON
    with open('empleados.json', 'r') as f:
        empleados = json.load(f)
    
    # Obtener la información del empleado
    empleado = empleados.get(empleado_id)
    if not empleado:
        print("Error: Empleado no encontrado.")
        return
    
    # Obtener la hora actual
    hora_actual = datetime.now().strftime('%H:%M')
    
    # Verificar la acción y registrar entrada o salida
    if accion == 'entrada':
        if hora_actual > '08:00':
            empleado['advertencia'] = 'Llegada tarde'
        empleado['hora_entrada'] = hora_actual
    elif accion == 'salida':
        if hora_actual < '18:00':
            empleado['advertencia'] = 'Salida temprano'
        empleado['hora_salida'] = hora_actual
    
    # Actualizar los datos del empleado en el archivo JSON
    with open('empleados.json', 'w') as f:
        json.dump(empleados, f, indent=4)
    
    # Registrar entrada/salida en archivo CSV
    with open('registro_empleados.csv', 'a', newline='') as csvfile:
        fieldnames = ['Empleado ID', 'Accion', 'Hora']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if accion == 'entrada':
            writer.writerow({'Empleado ID': empleado_id, 'Accion': 'Entrada', 'Hora': hora_actual})
            if 'advertencia' in empleado:
                writer.writerow({'Empleado ID': empleado_id, 'Accion': 'Advertencia', 'Hora': empleado['hora_entrada']})
        elif accion == 'salida':
            writer.writerow({'Empleado ID': empleado_id, 'Accion': 'Salida', 'Hora': hora_actual})
            if 'advertencia' in empleado:
                writer.writerow({'Empleado ID': empleado_id, 'Accion': 'Advertencia', 'Hora': empleado['hora_salida']})



