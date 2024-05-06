import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from crud import crear_plan, mostrar_planes,eliminar_plan,get_planID
from pymongo import MongoClient

def mostrar_planes_db():
    # Conexión a la base de datos MongoDB
    client = MongoClient('localhost', 27017)
    db = client['software']
    planes_collection = db['PLANES']

    # Obtener todos los planes de la colección
    planes = planes_collection.find()

    # Limpiar el contenido anterior en la pestaña de ver planes
    for child in ver_planes_treeview.get_children():
        ver_planes_treeview.delete(child)

    # Mostrar los planes en la pestaña de ver planes
    for plan in planes:
        ver_planes_treeview.insert('', 'end', values=(plan['CLAVE'], plan['CARRERA'], plan['MATERIA'],plan['FECHAALTA'],plan['FECHABAJA'],plan['REQSIM'],plan['REQUI1'],plan['REQUI2'],plan['REQUI3'],plan['REQUI4'],plan['SEMEST'],plan['AREA']))

    client.close()

def mostrar_materias_db():
    # Conexión a la base de datos MongoDB
    client = MongoClient('localhost', 27017)
    db = client['software']
    materias_collection = db['MATERIAS']

    # Obtener todas las materias de la colección
    materias = materias_collection.find()

    # Limpiar el contenido anterior en la pestaña de ver materias
    for child in ver_materias_treeview.get_children():
        ver_materias_treeview.delete(child)

    # Mostrar las materias en la pestaña de ver materias
    for materia in materias:
        ver_materias_treeview.insert('', 'end', values=(materia['CLAVE'], materia['NOMBRE']))

    client.close()

    
def insertar_plan():
    clave = clave_entry.get()
    carrera = int(carrera_entry.get())
    materia = int(materia_entry.get())
    fecha_alta = fecha_alta_entry.get()
    fechabaja = fechabaja_entry.get() or None
    area = area_entry.get() or None
    reqsim = int(reqsim_entry.get()) if reqsim_entry.get() else None
    requi1 = int(requi1_entry.get()) if requi1_entry.get() else None
    requi2 = int(requi2_entry.get()) if requi2_entry.get() else None
    requi3 = int(requi3_entry.get()) if requi3_entry.get() else None
    requi4 = int(requi4_entry.get()) if requi4_entry.get() else None
    semest = int(semest_entry.get())

    try:
        plan_creado = crear_plan(clave, carrera, materia, fecha_alta, fechabaja, area, reqsim, requi1, requi2, requi3, requi4, semest)
        if plan_creado ==0:
            messagebox.showerror("Error", "No se pudo insertar el plan")
            return
        else:   
            messagebox.showinfo("Éxito", "Plan insertado correctamente")
            mostrar_planes_db()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar el plan: {e}")
    

def actualizar_plan():
    clave = clave_entry.get()
    carrera = int(carrera_entry_a.get())
    materia = int(materia_entry_a.get())
    fecha_alta = fecha_alta_entry_a.get()
    fechabaja = fechabaja_entry_a.get() or None
    area = area_entry_a.get() or None
    reqsim = int(reqsim_entry_a.get()) if reqsim_entry_a.get() else None
    requi1 = int(requi1_entry_a.get()) if requi1_entry_a.get() else None
    requi2 = int(requi2_entry_a.get()) if requi2_entry_a.get() else None
    requi3 = int(requi3_entry_a.get()) if requi3_entry_a.get() else None
    requi4 = int(requi4_entry_a.get()) if requi4_entry_a.get() else None
    semest = int(semest_entry_a.get())

    try:
        plan_creado = actualizar_plan(clave, carrera, materia, fecha_alta, fechabaja, area, reqsim, requi1, requi2, requi3, requi4, semest)
        if plan_creado ==0:
            messagebox.showerror("Error", "No se pudo actualizar el plan")
            return
        else:   
            messagebox.showinfo("Éxito", "Plan actualizado correctamente")
            mostrar_planes_db()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar el plan: {e}")
def eliminar_plan_ui():
    # Obtener la carrera y la materia ingresadas por el usuario
    carrera = int(eliminar_carrera_entry.get())
    materia = int(eliminar_materia_entry.get())

    # Obtener el ID del plan
    print(carrera, materia)
    plan_id = get_planID(carrera, materia)
    print(plan_id)

    if plan_id:
        # Eliminar el plan
        eliminar_plan(plan_id)
        messagebox.showinfo("Éxito", "Plan eliminado correctamente")
        # Actualizar la vista de los planes
        mostrar_planes_db()
    else:
        messagebox.showerror("Error", "No se encontró ningún plan con la carrera y materia especificadas")


# Crear ventana principal
root = tk.Tk()
root.title("Sistema de Gestión de Planes")

# Crear el Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Función para crear una pestaña
def crear_pestana(notebook, titulo):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=titulo)
    return frame

# Pestaña para Insertar Plan
insertar_frame = crear_pestana(notebook, "Insertar Plan")

# Función para crear y alinear un label y un entry en la pestaña de insertar plan
def crear_label_entry_insertar(text):
    frame = tk.Frame(insertar_frame)
    frame.pack(pady=5)

    label = tk.Label(frame, text=text)
    label.pack(side="left", padx=(10, 5))

    entry = tk.Entry(frame)
    entry.pack(side="left", padx=(0, 10))
    return entry

clave_entry = crear_label_entry_insertar("Clave:")
carrera_entry = crear_label_entry_insertar("Carrera:")
materia_entry = crear_label_entry_insertar("Materia:")
fecha_alta_entry = crear_label_entry_insertar("Fecha de Alta (AAAA/MM/DD):")
fechabaja_entry = crear_label_entry_insertar("Fecha de Baja (AAAA/MM/DD):")
area_entry = crear_label_entry_insertar("Área:")
reqsim_entry = crear_label_entry_insertar("Requisito Similar:")
requi1_entry = crear_label_entry_insertar("Requisito 1:")
requi2_entry = crear_label_entry_insertar("Requisito 2:")
requi3_entry = crear_label_entry_insertar("Requisito 3:")
requi4_entry = crear_label_entry_insertar("Requisito 4:")
semest_entry = crear_label_entry_insertar("Semestre:")

insertar_btn = tk.Button(insertar_frame, text="Insertar Plan", command=insertar_plan)
insertar_btn.pack(pady=5)

# Pestaña para Actualizar Plan (vacía por ahora)
actualizar_frame = crear_pestana(notebook, "Actualizar Plan")

def crear_label_entry_actualizar(text):
    frame = tk.Frame(actualizar_frame)
    frame.pack(pady=5)

    label = tk.Label(frame, text=text)
    label.pack(side="left", padx=(10, 5))

    entry = tk.Entry(frame)
    entry.pack(side="left", padx=(0, 10))
    return entry

clave_entry_a = crear_label_entry_actualizar("Clave:")
carrera_entry_a = crear_label_entry_actualizar("Carrera:")
materia_entry_a = crear_label_entry_actualizar("Materia:")
fecha_alta_entry_a = crear_label_entry_actualizar("Fecha de Alta (AAAA/MM/DD):")
fechabaja_entry_a = crear_label_entry_actualizar("Fecha de Baja (AAAA/MM/DD):")
area_entry_a = crear_label_entry_actualizar("Área:")
reqsim_entry_a = crear_label_entry_actualizar("Requisito Similar:")
requi1_entry_a = crear_label_entry_actualizar("Requisito 1:")
requi2_entry_a = crear_label_entry_actualizar("Requisito 2:")
requi3_entry_a = crear_label_entry_actualizar("Requisito 3:")
requi4_entry_a = crear_label_entry_actualizar("Requisito 4:")
semest_entry_a = crear_label_entry_actualizar("Semestre:")

insertar_btn = tk.Button(actualizar_frame, text="Actualizar plan", command=actualizar_plan)
insertar_btn.pack(pady=5)

# Pestaña para Eliminar Plan (vacía por ahora)
eliminar_frame = crear_pestana(notebook, "Eliminar Plan")
# Función para crear y alinear un label y un entry en la pestaña de eliminar plan
def crear_label_entry_eliminar(text):
    frame = tk.Frame(eliminar_frame)
    frame.pack(pady=5)

    label = tk.Label(frame, text=text)
    label.pack(side="left", padx=(10, 5))

    entry = tk.Entry(frame)
    entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
    return entry

eliminar_carrera_entry = crear_label_entry_eliminar("Carrera:")
eliminar_materia_entry = crear_label_entry_eliminar("Materia:")

eliminar_btn = tk.Button(eliminar_frame, text="Eliminar Plan", command=eliminar_plan_ui)
eliminar_btn.pack(pady=5)

# Pestaña para Ver Planes
ver_planes_frame = crear_pestana(notebook, "Ver Planes")
ver_planes_treeview = ttk.Treeview(ver_planes_frame, columns=('clave', 'carrera', 'materia','fechaAlta','fechaBaja','reqsim','reqsim1','reqsim2','reqsim3','reqsim4','semest','area'))
ver_planes_treeview.heading('#0', text='')
ver_planes_treeview.heading('clave', text='Clave')
ver_planes_treeview.heading('carrera', text='Carrera')
ver_planes_treeview.heading('materia', text='Materia')
ver_planes_treeview.heading('fechaAlta', text='FechaAlta')
ver_planes_treeview.heading('fechaBaja', text='FechaBaja')
ver_planes_treeview.heading('reqsim', text='Reqsim')
ver_planes_treeview.heading('reqsim1', text='Reqsim1')
ver_planes_treeview.heading('reqsim2', text='Reqsim2')
ver_planes_treeview.heading('reqsim3', text='Reqsim3')
ver_planes_treeview.heading('reqsim4', text='Reqsim4')
ver_planes_treeview.heading('semest', text='Semest')
ver_planes_treeview.heading('area', text='Area')
ver_planes_treeview.column('#0', width=0, stretch=tk.NO)
ver_planes_treeview.column('clave', anchor=tk.W, width=100)
ver_planes_treeview.column('carrera', anchor=tk.W, width=100)
ver_planes_treeview.column('materia', anchor=tk.W, width=100)
ver_planes_treeview.column('fechaAlta', anchor=tk.W, width=100)
ver_planes_treeview.column('fechaBaja', anchor=tk.W, width=100)
ver_planes_treeview.column('reqsim', anchor=tk.W, width=100)
ver_planes_treeview.column('reqsim1', anchor=tk.W, width=100)
ver_planes_treeview.column('reqsim2', anchor=tk.W, width=100)
ver_planes_treeview.column('reqsim3', anchor=tk.W, width=100)
ver_planes_treeview.column('reqsim4', anchor=tk.W, width=100)
ver_planes_treeview.column('semest', anchor=tk.W, width=100)
ver_planes_treeview.column('area', anchor=tk.W, width=100)


ver_planes_treeview.pack(fill=tk.BOTH, expand=True)
# Llamar a la función para mostrar los planes
mostrar_planes_db()

# Pestaña para Ver Materias
ver_materias_frame = crear_pestana(notebook, "Ver Materias")
ver_materias_treeview = ttk.Treeview(ver_materias_frame, columns=('clave', 'nombre'))
ver_materias_treeview.heading('#0', text='')
ver_materias_treeview.heading('clave', text='Clave')
ver_materias_treeview.heading('nombre', text='Nombre')
ver_materias_treeview.column('#0', width=0, stretch=tk.NO)
ver_materias_treeview.column('clave', anchor=tk.W, width=100)
ver_materias_treeview.column('nombre', anchor=tk.W, width=200)
ver_materias_treeview.pack(fill=tk.BOTH, expand=True)
# Llamar a la función para mostrar las materias
mostrar_materias_db()

root.mainloop()
