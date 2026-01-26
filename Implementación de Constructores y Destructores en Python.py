#Estudiante Anthony Alberto Mantilla Armijos
# Clase 1: Ejemplo de un objeto simple (Un coche)
class Coche:
    # El constructor (__init__) sirve para dar valores iniciales
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"--> Constructor: Se ha fabricado un coche {self.marca} {self.modelo}")

    def conducir(self):
        print(f"    El {self.marca} está en movimiento...")

    # El destructor (__del__) se activa cuando borramos el objeto
    def __del__(self):
        print(f"<-- Destructor: El coche {self.marca} fue enviado al deshuesadero.")


# Clase 2: Ejemplo con manejo de recursos (Simulando una sesión)
class SesionUsuario:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.conectado = True
        print(f"--> Constructor: Iniciando sesión para el usuario '{nombre_usuario}'")

    def ver_perfil(self):
        if self.conectado:
            print(f"    Viendo perfil de {self.nombre_usuario}...")
        else:
            print("    Error: No hay conexión.")

    # Aquí el destructor es útil para cerrar la sesión automáticamente
    def __del__(self):
        if self.conectado:
            self.conectado = False
            print(f"<-- Destructor: Cerrando la sesión de '{self.nombre_usuario}' para liberar memoria.")


# --- Bloque de pruebas (Probando que las clases funcionen) ---

print("--- INICIO DE LA TAREA ---\n")

# 1. Probando la clase Coche
mi_auto = Coche("Toyota", "Corolla")
mi_auto.conducir()

# Borramos el auto manualmente para ver el destructor actuar ya
print("Voy a vender el auto...")
del mi_auto

print("\n--------------------------------\n")

# 2. Probando la clase SesionUsuario
usuario1 = SesionUsuario("Mantilla")
usuario1.ver_perfil()

# Nota: Aquí no uso 'del'. Quiero demostrar que Python llama al destructor solo cuando el programa termina.
print("\n--- FIN DEL PROGRAMA (El destructor de Mantilla se ejecutará abajo) ---")