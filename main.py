from pymongo import MongoClient
from crud import *
def mostrar_menu():
    print("1. Insertar Plan")
    print("2. Actualizar Plan")
    print("3. Eliminar Plan")
    print("4. Mostrar Planes")
    print("5. Mostrar Materias")
    opcion = input("Seleccione una opción (o 'q' para salir): ")
    return opcion

def procesar_opcion(opcion):
    if opcion == '1':
        print("Opción 1 seleccionada.")
        clave = input("Insertando Plan. Ingrese la clave (Letra Mayúscula):")
        carrera = input("Insertando Plan. Ingrese la carrera (número):")
        materia = input("Insertando Plan. Ingrese la materia (número):")
        fecha_alta = input("Insertando Plan. Ingrese la fecha de alta (AAAA/MM/DD):")
        fechabaja = input("Insertando Plan. Ingrese la fecha de baja (AAAA/MM/DD):")
        area = input("Insertando Plan. Ingrese el area (puede estar vacio):")
        reqsim = input("Insertando Plan. Ingrese el Requisito Similar (puede estar vacio):")
        requi1 = input("Insertando Plan. Ingrese el Requisito 1 (Número, puede estar vacio):")
        requi2 = input("Insertando Plan. Ingrese el Requisito 2 (Número, puede estar vacio):")
        requi3 = input("Insertando Plan. Ingrese el Requisito 3 (Número, puede estar vacio):")
        requi4 = input("Insertando Plan. Ingrese el Requisito 4 (Número, puede estar vacio):")
        semest = input("Insertando Plan. Ingrese el Semestre (número):")
        crear_plan(clave, carrera, materia, fecha_alta, fechabaja, area, reqsim, requi1, requi2, requi3, requi4, semest)
    elif opcion == '2':
        print("Opción 2 seleccionada.")
        buscar_plan1 = int(input("Buscando Plan. Ingrese la carrera(número):"))
        buscar_plan2 = int(input("Buscando Plan. Ingrese la materia(número):"))
        plan_id = get_planID(buscar_plan1, buscar_plan2)
        if plan_id:
            clave = input("Actualizando Plan. Ingrese la clave (Letra Mayúscula):")
            carrera = input("Actualizando Plan. Ingrese la carrera (número):")
            materia = input("Actualizando Plan. Ingrese la materia (número):")
            fecha_alta = input("Actualizando Plan. Ingrese la fecha de alta (AAAA/MM/DD):")
            fechabaja = input("Actualizando Plan. Ingrese la fecha de baja (AAAA/MM/DD):")
            area = input("Actualizando Plan. Ingrese el area (puede estar vacio):")
            reqsim = input("Actualizando Plan. Ingrese el Requisito Similar (puede estar vacio):")
            requi1 = input("Actualizando Plan. Ingrese el Requisito 1 (Número, puede estar vacio):")
            requi2 = input("Actualizando Plan. Ingrese el Requisito 2 (Número, puede estar vacio):")
            requi3 = input("Actualizando Plan. Ingrese el Requisito 3 (Número, puede estar vacio):")
            requi4 = input("Actualizando Plan. Ingrese el Requisito 4 (Número, puede estar vacio):")
            semest = input("Actualizando Plan. Ingrese el Semestre (número):")
            actualizar_plan(plan_id, clave, carrera, materia, fecha_alta, fechabaja, area, reqsim, requi1, requi2, requi3, requi4, semest)
    elif opcion == '3':
        print("Opción 3 seleccionada.")
        buscar_plan1 = int(input("Eliminando Plan. Ingrese la carrera(número):"))
        buscar_plan2 = int(input("Eliminando Plan. Ingrese la materia(número):"))
        plan_id = get_planID(buscar_plan1, buscar_plan2)
        if plan_id:
            eliminar_plan(plan_id)
    elif opcion == '4':
        print("Opción 4 seleccionada.")
        mostrar_planes()
    elif opcion == '5':
        print("Opción 5 seleccionada.")
        mostrar_materias()
    elif opcion.lower() == 'q':
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    """Función principal del programa."""
    while True:
        opcion = mostrar_menu()
        procesar_opcion(opcion)
        if opcion.lower() == 'q':
            break

def mostrar_materias():
    client = MongoClient('localhost', 27017)  
    db = client['software']
    collection = db['MATERIAS']

    doc = collection.find()
    print("Materias:")
    for d in doc:
        print(f"  CLAVE:{d['CLAVE']} - NOMBRE:{d['NOMBRE']}")    
    client.close()
    
if __name__ == "__main__":
    main()
