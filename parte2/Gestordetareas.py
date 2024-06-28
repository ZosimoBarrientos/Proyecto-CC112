# Lista global para almacenar las tareas.
tasks = []

# Función para agregar una tarea a la lista.
def addtask(description):
  tasks.append({"description": description, "completed": False})
  print(f'Tarea "{description}" agregada.')

# Función para eliminar una tarea de la lista por su índice.
def deletetask(index):
  if 0 <= index < len(tasks):
    removed_task = tasks.pop(index)
    print(f'Tarea "{removed_task["description"]}" eliminada.')
  else:
    print("Indice invalido.")

# Función para marcar una tarea como completada por su índice.
def completetask(index):
  if 0 <= index < len(tasks):
    tasks[index]["completed"] = True
    print(f'Tarea "{tasks[index]["description"]}" marcada como completada.')
  else:
    print("Indice invalido.")

# Función para mostrar todas las tareas.
def showtasks():
  if not tasks:
    print("No hay tareas.")
  else:
    for i, task in enumerate(tasks):
      status = "X" if task["completed"] else " "
      print(f"{i}. [{status}] {task['description']}")

# Función principal para manejar la interfaz de usuario.
def main():
  while True:
    print("\nGestion de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Completar tarea")
    print("4. Mostrar tareas")
    print("5. Salir")

    choice = input("Seleccione una opcion: ")

    if choice == "1":
      description = input("Descripcion de la tarea: ")
      addtask(description)
    elif choice == "2":
      index = int(input("Indice de la tarea a eliminar: "))
      deletetask(index)
    elif choice == "3":
      index = int(input("Indice de la tarea a completar: "))
      completetask(index)
    elif choice == "4":
      showtasks()
    elif choice == "5":
      print("Saliendo del programa.")
      break
    else:
      print("Opcion invalida. Intente de nuevo.")

# Ejecutar la función principal si este archivo se ejecuta directamente.
if __name__ == "__main__":
    main()