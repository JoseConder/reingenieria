from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['software']
collection = db['PLANES']
carreras = db['CARRERAS']
materias = db['MATERIAS']

def verificar_carrera(clave_carrera):
    carrera_existente = carreras.find_one({'CLAVE': clave_carrera})
    if not carrera_existente:
        print(f"Error: La carrera con clave {clave_carrera} no existe.")
        return False
    else:
        print(f"La carrera con clave {clave_carrera} existe.")
    return True

def verificar_materia(clave_materia):
    materia_existente = materias.find_one({'CLAVE': clave_materia})
    if not materia_existente:
        print(f"Error: La materia con clave {clave_materia} no existe.")
        return False
    else:
        print(f"La materia con clave {clave_materia} existe.")
    return True

def verificar_requisitos(requisitos):
    for requisito in requisitos:
        if requisito and not verificar_materia(requisito):
            print(f"Error: El requisito {requisito} no existe.")
            return False
    print("Todos los requisitos existen.")
    return True

def verificar_plan(plan_id):
    plan_existente = collection.find_one({'_id': ObjectId(plan_id)})
    if not plan_existente:
        print(f"Error: El plan con ID {plan_id} no existe.")
        return False
    else:
        print(f"El plan con ID {plan_id} existe.")
    return True

def crear_plan(clave, carrera, materia, fecha_alta, fechabaja=None, area=None, reqsim=None, requi1=None, requi2=None, requi3=None, requi4=None, semest=None):
    if not verificar_carrera(carrera):
        print("No se pudo crear el plan. Verifica la carrera.")
        return
    if not verificar_materia(materia):
        print("No se pudo crear el plan. Verifica la materia.")
        return
    requisitos = [reqsim, requi1, requi2, requi3, requi4]
    if not verificar_requisitos(requisitos):
        print("No se pudo crear el plan. Verifica los requisitos.")
        return
    
    nuevo_plan = {
        'CLAVE': clave,
        'CARRERA': carrera,
        'MATERIA': materia,
        'FECHAALTA': fecha_alta,
        'FECHABAJA': fechabaja,
        'AREA': area,
        'REQSIM': reqsim,
        'REQUI1': requi1,
        'REQUI2': requi2,
        'REQUI3': requi3,
        'REQUI4': requi4,
        'SEMEST': semest
    }
    resultado = collection.insert_one(nuevo_plan)
    print(f"Nuevo plan creado con el ID: {resultado.inserted_id}, para la materia: {materia}")

def actualizar_plan(plan_id, clave, carrera, materia, fecha_alta, fechabaja=None, area=None, reqsim=None, requi1=None, requi2=None, requi3=None, requi4=None, semest=None):
    if not verificar_plan(plan_id):
        print("No se pudo actualizar el plan. Verifica el plan.")
        return
    if not verificar_carrera(carrera):
        print("No se pudo crear el plan. Verifica la carrera.")
        return
    if not verificar_materia(materia):
        print("No se pudo crear el plan. Verifica la materia.")
        return
    requisitos = [reqsim, requi1, requi2, requi3, requi4]
    if not verificar_requisitos(requisitos):
        print("No se pudo crear el plan. Verifica los requisitos.")
        return
    filtro = {'_id': ObjectId(plan_id)}
    nuevo_valor = {
        '$set': {
            'CLAVE': clave,
            'CARRERA': carrera,
            'MATERIA': materia,
            'FECHAALTA': fecha_alta,
            'FECHABAJA': fechabaja,
            'AREA': area,
            'REQSIM': reqsim,
            'REQUI1': requi1,
            'REQUI2': requi2,
            'REQUI3': requi3,
            'REQUI4': requi4,
            'SEMEST': semest
        }
    }
    collection.update_one(filtro, nuevo_valor)
    print(f"Se actualizó correctamente el plan con el ID: {plan_id}")

def eliminar_plan(plan_id):
    if not verificar_plan(plan_id):
        print("No se pudo eliminar el plan. Verifica el plan.")
        return
    filtro = {'_id': ObjectId(plan_id)}
    collection.delete_one(filtro)
    print(f"Se eliminó correctamente el plan con el ID: {plan_id}")

def get_planID(carrera, materia):
    plan = collection.find_one({'CARRERA': carrera, 'MATERIA': materia})
    if plan:
        return plan['_id']
    else:
        print("No se encontro el plan.")
        return None
    
def mostrar_planes():
    client = MongoClient('localhost', 27017)  
    db = client['software']
    collection = db['PLANES']

    doc = collection.find()
    print("Planes:")
    for d in doc:
        requisitos = []
        for req in [d['REQSIM'], d['REQUI1'], d['REQUI2'], d['REQUI3'], d['REQUI4']]:
            if isinstance(req, dict):
                requisitos.append(req['MATERIA'])
        requisitos_str = ', '.join(map(str, requisitos))
        print(f"  Clave: {d['CLAVE']} - Carrera: {d['CARRERA']} - Materia: {d['MATERIA']} - Fecha de Alta: {d['FECHAALTA']} - Fecha de Baja: {d['FECHABAJA']} - Requisitos: {requisitos_str} - Semestre: {d['SEMEST']} - Area: {d['AREA']}")
    client.close()


