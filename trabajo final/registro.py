import json

class Registro:
    def __init__(self):
        self.lista = []

    def cargar_datos(self):
        try:
            with open('usuarios.json', 'r') as archivo:
                self.lista = json.load(archivo)
        except FileNotFoundError:
            self.lista = []

    def guardar_datos(self):
        with open('usuarios.json', 'w') as archivo:
            json.dump(self.lista, archivo)

    def agregar_usuario(self, nombre):
        for contacto in self.lista:
            if contacto['nombre'] == nombre:
                print("Este usuario ya existe.")
                return
        nuevo_registro = {'nombre': nombre}
        self.lista.append(nuevo_registro)
        print("Nuevo usuario agregado exitosamente.")
        self.guardar_datos()

    def mostrar_usuario(self):
        if not self.lista:
            print("No hay usuarios registrados.")
        else:
            print("\nLista de usuarios:")
            for i, registro in enumerate(self.lista):
                print(f"{i + 1}. {registro['nombre']}")

    def buscar_usuario(self, nombre):
        for registro in self.lista:
            if registro['nombre'] == nombre:
                print(f"Usuario encontrado: {registro['nombre']}")
                return
        print("Usuario no encontrado.")

    def eliminar_usuario(self, nombre):
        for i, registro in enumerate(self.lista):
            if registro['nombre'] == nombre:
                del self.lista[i]
                print("Usuario eliminado exitosamente.")
                self.guardar_datos()
                return
        print("Usuario no encontrado.")

if __name__ == "__main__":
    registro = Registro()
    registro.cargar_datos()

    while True:
        print("\nMenú:")
        print("1. Agregar usuario")
        print("2. Mostrar usuario")
        print("3. Buscar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el usuario: ")
            registro.agregar_usuario(nombre)
        elif opcion == '2':
            registro.mostrar_usuario()
        elif opcion == '3':
            nombre = input("Ingrese el usuario a buscar: ")
            registro.buscar_usuario(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el usuario a eliminar: ")
            registro.eliminar_usuario(nombre)
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
#importamos el codigo principal al registro
import pacman