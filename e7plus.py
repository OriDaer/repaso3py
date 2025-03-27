def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada):
    nueva_tarea = {"Tarea": tarea, "Fecha límite": fecha_limite, "Prioridad": prioridad, "Completada": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def marcar_completada(tareas):
    num_tarea = int(input("Ingrese el índice de la tarea que desea marcar como completada: ")) - 1
    if 0 <= num_tarea < len(tareas):
        tareas[num_tarea]["Completada"] = True
        print("Tarea marcada como completada exitosamente.")
    else:
        print("Error. Tarea no encontrada.")

def mostrar_tareas(tareas, completadas=None):
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    for i, tarea in enumerate(tareas, 1):
        if completadas == None or tarea["Completada"] == completadas:
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")

if __name__ == "__main__":
    lista_tareas = []
    
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Salir")
        print("4. Marcar tarea como completada")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva, False)
        
        elif opcion == "2":
            mostrar_tareas(lista_tareas)
        
        elif opcion == "3":
            break
        
        elif opcion == "4":
            marcar_completada(lista_tareas)
    
        else:
            print("Opción no válida. Intente de nuevo.")
