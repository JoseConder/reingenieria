import pandas as pd
from pymongo import MongoClient

tipo = ''
loop = True

while loop:
    print("Ingresa que tipo de datos insertar en la base de datos:")
    print("Planes")
    print("Carreras")
    print("Materias")
    print("Salir")
    tipo = input().upper()

    if tipo == 'PLANES':
        client = MongoClient('localhost', 27017)  
        db = client['software']
        collection = db[tipo]  

        df = pd.read_csv('PLANES.csv', delimiter=',')

        # Insertar las materias en la colección PLANES y obtener sus _id
        materias = df[['CLAVE', 'CARRERA', 'MATERIA']].drop_duplicates()
        materias_dict = materias.to_dict(orient='records')
        materias_ids = collection.insert_many(materias_dict).inserted_ids

        # Convertir el DataFrame a un diccionario para insertar en MongoDB
        data = df.to_dict(orient='records')

        # Reemplazar los códigos de materia con las referencias correspondientes
        for record in data:
            for req_field in ['REQSIM', 'REQUI1', 'REQUI2', 'REQUI3', 'REQUI4']:
                if not pd.isnull(record[req_field]):
                    # Buscar el documento de la materia referenciada
                    materia_ref = next(m for m in materias_dict if m['MATERIA'] == record[req_field])
                    # Agregar la materia referenciada al documento principal
                    record[req_field] = materia_ref

        collection.insert_many(data)

        print("Datos insertados en MongoDB correctamente.")

        collection.delete_many({ 
            'REQSIM': {'$exists': False}, 
            'REQUI1': {'$exists': False}, 
            'REQUI2': {'$exists': False}, 
            'REQUI3': {'$exists': False}, 
            'REQUI4': {'$exists': False} 
        })

        print("Documentos duplicados sin referencias eliminados correctamente.")

        client.close()
    elif tipo == 'CARRERAS' or tipo == 'MATERIAS':
        client = MongoClient('localhost', 27017)  
        db = client['software']
        collection = db[tipo]  

        df = pd.read_csv(tipo + '.csv', delimiter=',')

        data = df.to_dict(orient='records')

        collection.insert_many(data)

        print("Datos insertados en MongoDB correctamente.")
    else:
        loop = False
