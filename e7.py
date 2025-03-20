tareas = []

while True:
    descripcion = input("Descripción de la tarea (o 'salir' para terminar): ")
    if descripcion == "salir" or descripcion=='Salir':
        print("Saliendo...")
        False
        break
    fecha = input("Fecha límite: ")
    prioridad = input("Prioridad (Alta, Media, Baja): ")
    tareas.append({"Descripción": descripcion, "Fecha límite": fecha, "Prioridad": prioridad})
    print("TAREAS:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. Descripción: {tarea['Descripción']} - Fecha: {tarea['Fecha límite']} - Prioridad: {tarea['Prioridad']}")