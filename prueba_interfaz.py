import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from crud import crear_plan, mostrar_planes
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
        ver_planes_treeview.insert('', 'end', values=(plan['CLAVE'], plan['CARRERA'], plan['MATERIA']))

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
            mostrar_planes()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo insertar el plan: {e}")

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

tk.Label(insertar_frame, text="Clave:").grid(row=0, column=0)
clave_entry = tk.Entry(insertar_frame)
clave_entry.grid(row=0, column=1)

tk.Label(insertar_frame, text="Carrera:").grid(row=1, column=0)
carrera_entry = tk.Entry(insertar_frame)
carrera_entry.grid(row=1, column=1)

tk.Label(insertar_frame, text="Materia:").grid(row=2, column=0)
materia_entry = tk.Entry(insertar_frame)
materia_entry.grid(row=2, column=1)

tk.Label(insertar_frame, text="Fecha de Alta (AAAA/MM/DD):").grid(row=3, column=0)
fecha_alta_entry = tk.Entry(insertar_frame)
fecha_alta_entry.grid(row=3, column=1)

tk.Label(insertar_frame, text="Fecha de Baja (AAAA/MM/DD):").grid(row=4, column=0)
fechabaja_entry = tk.Entry(insertar_frame)
fechabaja_entry.grid(row=4, column=1)

tk.Label(insertar_frame, text="Área:").grid(row=5, column=0)
area_entry = tk.Entry(insertar_frame)
area_entry.grid(row=5, column=1)

tk.Label(insertar_frame, text="Requisito Similar:").grid(row=6, column=0)
reqsim_entry = tk.Entry(insertar_frame)
reqsim_entry.grid(row=6, column=1)

tk.Label(insertar_frame, text="Requisito 1:").grid(row=7, column=0)
requi1_entry = tk.Entry(insertar_frame)
requi1_entry.grid(row=7, column=1)

tk.Label(insertar_frame, text="Requisito 2:").grid(row=8, column=0)
requi2_entry = tk.Entry(insertar_frame)
requi2_entry.grid(row=8, column=1)

tk.Label(insertar_frame, text="Requisito 3:").grid(row=9, column=0)
requi3_entry = tk.Entry(insertar_frame)
requi3_entry.grid(row=9, column=1)

tk.Label(insertar_frame, text="Requisito 4:").grid(row=10, column=0)
requi4_entry = tk.Entry(insertar_frame)
requi4_entry.grid(row=10, column=1)

tk.Label(insertar_frame, text="Semestre:").grid(row=11, column=0)
semest_entry = tk.Entry(insertar_frame)
semest_entry.grid(row=11, column=1)

insertar_btn = tk.Button(insertar_frame, text="Insertar Plan", command=insertar_plan)
insertar_btn.grid(row=12, column=0, columnspan=2, pady=10)

# Pestaña para Actualizar Plan (vacía por ahora)
actualizar_frame = crear_pestana(notebook, "Actualizar Plan")

# Pestaña para Eliminar Plan (vacía por ahora)
eliminar_frame = crear_pestana(notebook, "Eliminar Plan")

# Pestaña para Ver Planes
ver_planes_frame = crear_pestana(notebook, "Ver Planes")
ver_planes_treeview = ttk.Treeview(ver_planes_frame, columns=('clave', 'carrera', 'materia'))
ver_planes_treeview.heading('#0', text='')
ver_planes_treeview.heading('clave', text='Clave')
ver_planes_treeview.heading('carrera', text='Carrera')
ver_planes_treeview.heading('materia', text='Materia')
ver_planes_treeview.column('#0', width=0, stretch=tk.NO)
ver_planes_treeview.column('clave', anchor=tk.W, width=100)
ver_planes_treeview.column('carrera', anchor=tk.W, width=100)
ver_planes_treeview.column('materia', anchor=tk.W, width=100)
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
