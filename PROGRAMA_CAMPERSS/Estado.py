import Matricula

def matricula_camper():
    matriculas={}
    print("Bienvenido a matriculación")
    print("Camper que pasaron la prueba inicial ")
    matriculas["nom_matricula"] = input("nombre_del_camper")
    matriculas["Estado"] = "En proceso de inscricion"
 
    Matricula.data.append(matriculas)
    Matricula.guardar_datos()
   
    
def mostrar_camper_admitidos():
    print("Los Campers registrados son:")
    for matriculas in Matricula.data: 
        print("Camper que paso la prueba", matriculas["nom_matricula"], "Esta" , matriculas ["Estado"])