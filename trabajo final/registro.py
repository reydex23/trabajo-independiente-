registro = []
import json

def cargar_datos():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open('usuarios.json', 'w') as archivo:
        json.dump(datos, archivo)

registro = cargar_datos()

def agregar_usuario():
    nombre = input("Ingrese el usuario: ")
    for contacto in registro:
        if contacto['nombre'] == nombre:
            print("este usuario ya existe.")
            return
    nuevo_registro = {'nombre': nombre}
    registro.append(nuevo_registro)
    print("nuevo usuario agregado exitosamente.")
    guardar_datos(registro)
def mostrar_usuario():
    if not registro:
        print("No hay usuarios registrados.")
    else:
        print("\nLista de usuarios:")
        for i, registro in enumerate(registro):
            print(f"{i+1}. {registro['nombre']}")
def buscar_usuario():
    nombre = input("Ingrese el usuario a buscar: ")
    for registro in registro:
        if registro['nombre'] == nombre:
            print(f"usuario encontrado: {registro['nombre']}")
            return
    print("usuario no encontrado.")
def eliminar_usuario():
    nombre = input("Ingrese el usuario a eliminar: ")
    for i, registro in enumerate(registro):
        if registro['nombre'] == nombre:
            del registro[i]
            print("usuario eliminado exitosamente.")
            return
    print("usuario no encontrado.")
while True:
    print("\nMenú:")
    print("1. Agregar usuario")
    print("2. Mostrar usuario")
    print("3. Buscar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        agregar_usuario()
    elif opcion == '2':
        mostrar_usuario()
    elif opcion == '3':
        buscar_usuario()
    elif opcion == '4':
        eliminar_usuario()
    elif opcion == '5':
        break
    else:
        print("Opción inválida.")