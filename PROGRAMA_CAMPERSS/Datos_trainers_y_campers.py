def imprimir_datos_trainer_camper(doc_trainer, doc_camper):
    global data
    
    if doc_trainer in data:
        trainer = data[doc_trainer]
        print("Datos del Trainer:")
        print(f"Documento: {doc_trainer}")
        print(f"Nombre: {trainer.get('Nombre', '')}")
        print(f"Apellidos: {trainer.get('Apellidos', '')}")
        print(f"Dirección: {trainer.get('Direccion', '')}")
        print(f"Número de teléfono: {trainer.get('Telefono', '')}")
        print(f"Horario: {trainer.get('Horario', '')}")
        print(f"Área: {trainer.get('Area', '')}")
        print(f"Grupo: {trainer.get('Grupo trainer', '')}")
    else:
        print("No se encontró información para el Trainer con ese documento.")

    if doc_camper in data:
        camper = data[doc_camper]
        print("\nDatos del Camper:")
        print(f"Documento: {doc_camper}")
        print(f"Nombre: {camper.get('Nombre', '')}")
        print(f"Apellidos: {camper.get('apellido', '')}")
        print(f"Dirección: {camper.get('direccion', '')}")
        print(f"Acudiente: {camper.get('acudiente', '')}")
        print(f"Número de teléfono: {camper.get('telefono', '')}")
        print(f"Estado: {camper.get('Estado', '')}")
        print(f"Riesgo: {camper.get('Riesgo', '')}")
        print(f"Ruta: {camper.get('Ruta', '')}")
        print(f"Nota: {camper.get('Nota', '')}")
        print(f"Grupo: {camper.get('Grupo', '')}")
    else:
        print("No se encontró información para el Camper con ese documento.")
