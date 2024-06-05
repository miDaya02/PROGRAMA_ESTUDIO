def agrupar_y_imprimir(data):
    trainers_por_grupo = {}
    campers_por_grupo = {}

    for doc, info in data.items():
        if "grupo del trainer" in info:
            grupo = info["grupo del trainer"]
            trainers_por_grupo.setdefault(grupo, []).append((doc, info["Nombre"], info["apellido"]))

    for doc, info in data.items():
        if "grupo" in info:
            grupo = info["grupo"]
            campers_por_grupo.setdefault(grupo, []).append((doc, info["Nombre"], info["apellido"]))

    print("Trainers y Campers por Grupo:")
    for grupo in trainers_por_grupo.keys() | campers_por_grupo.keys():
        print(f"Grupo: {grupo}")
        print("Trainers:")
        for doc, nombre, apellido in trainers_por_grupo.get(grupo, []):
            print(f"  Documento: {doc}, Nombre: {nombre} {apellido}")
        print("Campers:")
        for doc, nombre, apellido in campers_por_grupo.get(grupo, []):
            print(f"  Documento: {doc}, Nombre: {nombre} {apellido}")
        print()