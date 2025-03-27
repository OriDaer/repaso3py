
def agregar_tarea(tareas, tarea, fecha_limite, prioridad,completada):
    nueva_tarea = {"Tarea": tarea, "Fecha límite": fecha_limite, "Prioridad": prioridad, "Completada": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")
def marcar_completada(tareas):
    numTarea=input('ingrese el indice de la tarea que desea marcar como completada: ')
    if tareas[numTarea]["Completada"] in tareas:
        tareas[numTarea]["Completada"] = True
        print("Tarea marcada como completada exitosamente.")
    else:
        print("Error.Tarea no encontrada.")
def mostrar_tareas (tareas,completadas):
    if completadas==True:
        for tarea in tareas:
            if tarea["Completada"]==True:
                print(f"Tarea: {tarea['Tarea']}, Fecha límite: {tarea['Fecha límite']}, Prioridad: {tarea['Prioridad']}, Completada: {tarea['Completada']}")
    if completadas==False:
        for tarea in tareas:
            if tarea["Completada"]==False:
                print(f"Tarea: {tarea['Tarea']}, Fecha límite: {tarea['Fecha límite']}, Prioridad: {tarea['Prioridad']}, Completada: {tarea['Completada']}")
    if not completadas or completadas==None:
        for i, tarea in enumerate(tareas, 1):
                    print(f"\nTarea {i}:")
                    for clave, valor in tarea.items():
                        print(f"{clave}: {valor}")
    if not tareas:
        print("No hay tareas pendientes.")

if __name__ == "__main__":
    lista_tareas = []
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        print("4. Marcar tarea como completada")
        opcion = input("Seleccione una opción: ")
        if opcion=="1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = int(input("Ingrese la fecha límite (formato: dd/mm/yyyy): "))
            prioridad_nueva = input("Ingrese la prioridad: ")
            completada_nueva = False
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva, completada_nueva)
        elif opcion == "2":
            mostrar_tareas (lista_tareas,completada_nueva)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        if opcion == "4":
            marcar_completada(lista_tareas)
