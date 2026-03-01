import json
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # (para obtener los valores)
    def get_id(self): return self.__id_producto

    def get_nombre(self): return self.__nombre

    def get_cantidad(self): return self.__cantidad

    def get_precio(self): return self.__precio

    # (para modificar los valores)
    def set_cantidad(self, cantidad): self.__cantidad = cantidad

    def set_precio(self, precio): self.__precio = precio

    def set_nombre(self, nombre): self.__nombre = nombre

    # Metodo para convertir el objeto a un formato que JSON pueda entender
    def to_dict(self):
        return {
            "id": self.__id_producto,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    def __str__(self):
        return f"ID: {self.__id_producto} | Producto: {self.__nombre} | Cant: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# CLASE INVENTARIO (Ahora usando Diccionario y JSON)
class Inventario:
    def __init__(self):
        # La clave (key) será el ID, y el valor (value) será el objeto Producto
        self.productos = {}
        self.archivo = "inventario_makaco.json"
        self.cargar_inventario()  # Carga los datos automáticamente al arrancar

    # --- SERIALIZACIÓN Y PERSISTENCIA DE ARCHIVOS ---
    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                # Convertimos todos los objetos Producto a diccionarios simples para guardarlos
                datos_serializados = {id_prod: prod.to_dict() for id_prod, prod in self.productos.items()}
                json.dump(datos_serializados, f, indent=4)  # json.dump escribe en el archivo
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_inventario(self):
        # Reconstruimos los objetos Producto a partir de los datos leídos
        # Si el archivo no existe aún (primera vez que se corre), no pasa nada
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)  # json.load lee (deserializa) el archivo
                self.productos = {id_prod: Producto(p['id'], p['nombre'], p['cantidad'], p['precio']) for id_prod, p in
                                  datos.items()}
        except FileNotFoundError:
            self.productos = {}
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    # MÉTODOS DE GESTIÓN
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_inventario()
            print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]  # Eliminar de un diccionario es rapidísimo
            self.guardar_inventario()
            print("✅ Producto eliminado con éxito.")
        else:
            print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].set_precio(nuevo_precio)
            self.guardar_inventario()
            print("✅ Producto actualizado con éxito.")
        else:
            print("❌ Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Buscamos coincidencias en los nombres, sin importar mayúsculas o minúsculas
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("\n--- Resultados de Búsqueda ---")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("\n--- Inventario Actual ---")
            for p in self.productos.values():
                print(p)
        else:
            print("⚠️ El inventario está vacío.")


# ==========================================
# MENÚ INTERACTIVO (Interfaz de Usuario)
# ==========================================
def menu():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 30)
        print("📦 SISTEMA DE INVENTARIO UEA 3.0")
        print("=" * 30)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            id_prod = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_prod = Producto(id_prod, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_prod)
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero y el precio un número válido.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            cant = input("Nueva cantidad (presione Enter para no cambiarla): ")
            prec = input("Nuevo precio (presione Enter para no cambiarlo): ")

            # Convertimos si el usuario escribió algo, sino mandamos None
            cant_val = int(cant) if cant.strip() else None
            prec_val = float(prec) if prec.strip() else None

            inventario.actualizar_producto(id_prod, cant_val, prec_val)

        elif opcion == '4':
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Guardando datos y saliendo del sistema... ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()


    #Actualizaciones 3.0:
    #La librería json: Cumple con el requisito de "Serialización y almacenamiento".
    #Cuando se guarda el archivo, ahora se crea un documento inventario_makaco.json que organiza los datos de forma estructurada y profesional, evitando los errores que daban los archivos .txt simples al leer líneas.
    #self.productos = {}): Ahora al buscar un producto por su ID es inmediato porque el ID funciona como una llave exacta, sin tener que recorrer toda una lista.
