# --- CLASES (Lógica del Sistema) ---

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos_base = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}] {self.datos_base[0]} - {self.datos_base[1]} ({self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista dinámica

    def __str__(self):
        titulos = ", ".join([l.datos_base[0] for l in self.libros_prestados]) or "Ninguno"
        return f"ID: {self.user_id} | Usuario: {self.nombre} | Prestados: {titulos}"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}  # {isbn: Libro}
        self.registro_ids = set()  # IDs únicos
        self.usuarios = {}  # {id: Usuario}

    def registrar_libro(self, titulo, autor, categoria, isbn):
        if isbn not in self.catalogo:
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            self.catalogo[isbn] = nuevo_libro
            print(f"✅ Libro registrado: {titulo}")
        else:
            print("⚠️ El ISBN ya existe.")

    def registrar_usuario(self, nombre, user_id):
        if user_id not in self.registro_ids:
            nuevo_usuario = Usuario(nombre, user_id)
            self.registro_ids.add(user_id)
            self.usuarios[user_id] = nuevo_usuario
            print(f"✅ Usuario {nombre} registrado con éxito.")
        else:
            print("⚠️ El ID de usuario ya está en uso.")

    def prestar(self, isbn, user_id):
        if isbn in self.catalogo and user_id in self.usuarios:
            libro = self.catalogo.pop(isbn)
            self.usuarios[user_id].libros_prestados.append(libro)
            print(f"📖 '{libro.datos_base[0]}' prestado a {self.usuarios[user_id].nombre}.")
        else:
            print("❌ Error: ISBN o ID de usuario no válidos.")

    def devolver(self, isbn, user_id):
        if user_id in self.usuarios:
            user = self.usuarios[user_id]
            for i, libro in enumerate(user.libros_prestados):
                if libro.isbn == isbn:
                    libro_devuelto = user.libros_prestados.pop(i)
                    self.catalogo[isbn] = libro_devuelto
                    print(f"✔ Libro '{libro_devuelto.datos_base[0]}' devuelto.")
                    return
            print("❌ El usuario no tiene ese libro.")
        else:
            print("❌ Usuario no encontrado.")

    def mostrar_catalogo(self):
        print("\n--- Libros Disponibles ---")
        if not self.catalogo: print("Vacío.")
        for l in self.catalogo.values(): print(l)


# --- MENÚ INTERACTIVO ---

def menu():
    biblio = Biblioteca()

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA DIGITAL UEA 4 ---")
        print("1. Registrar Libro")
        print("2. Registrar Usuario")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Ver Catálogo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            t = input("Título: ");
            a = input("Autor: ")
            c = input("Categoría: ");
            i = input("ISBN: ")
            biblio.registrar_libro(t, a, c, i)

        elif opcion == "2":
            n = input("Nombre: ");
            uid = input("ID de Usuario: ")
            biblio.registrar_usuario(n, uid)

        elif opcion == "3":
            i = input("ISBN del libro: ");
            uid = input("su ID de Usuario: ")
            biblio.prestar(i, uid)

        elif opcion == "4":
            i = input("ISBN del libro: ");
            uid = input("su ID de Usuario: ")
            biblio.devolver(i, uid)

        elif opcion == "5":
            biblio.mostrar_catalogo()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


# Arrancar el programa
if __name__ == "__main__":
    menu()