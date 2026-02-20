class Producto:
    """
    Le actualizare para que sea mas dinamico el interfaz con el usuario agregando iconos de error y listo
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters (Permiten leer los atributos)
    def get_id(self): return self.id_producto

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    # Setters (Permiten modificar los atributos de forma controlada)
    def set_nombre(self, nombre): self.nombre = nombre

    def set_cantidad(self, cantidad): self.cantidad = cantidad

    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        # Formato amigable para mostrar el producto en la consola
        return f"[ID: {self.id_producto}] {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """
    La mejor decisión de diseño sería agregarle un tipo
    Diccionario para que las búsquedas por ID sean más rápidas.
    """

    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Decisión de diseño: Validar que el ID sea único antes de agregarlo para evitar duplicados.
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("\nError: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("\n✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("\n✅ Producto eliminado.")
                return
        print("\n❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                print(f"Actualizando: {p.get_nombre()}")
                # Supuesto: El usuario puede presionar Enter si no quiere cambiar un valor específico.
                nueva_cant = input("Nueva cantidad (Presiona Enter para omitir): ")
                nuevo_precio = input("Nuevo precio (Presiona Enter para omitir): ")

                if nueva_cant:
                    p.set_cantidad(int(nueva_cant))
                if nuevo_precio:
                    p.set_precio(float(nuevo_precio))

                print("\n✅ Producto actualizado.")
                return
        print("\n❌ Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = False
        print(f"\nResultados de búsqueda para '{nombre}':")
        for p in self.productos:
            # Decisión de diseño: Convertimos todo a minúsculas (.lower()) para que
            # encuentre coincidencias sin importar si el usuario usa mayúsculas.
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrados = True
        if not encontrados:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)
        print("-------------------------")


def menu():
    inv = Inventario()

    while True:
        print("\n" + "=" * 30)
        print(" SISTEMA DE GESTIÓN DE INVENTARIO UEA 2.0")
        print("=" * 30)
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            """
            Añadire un Try Except ValueError por si el usuario escribe letras en lugar de numeros
            """
            try:
                id_p = input("ID del producto: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad en stock: "))
                pre = float(input("Precio: $"))
                inv.añadir_producto(Producto(id_p, nom, cant, pre))
            except ValueError:
                # Añadimos un bloque try-except básico
                print("\n❌ Error: La cantidad y el precio deben ser valores numéricos.")

        elif opcion == '2':
            inv.eliminar_producto(input("Ingresa el ID del producto a eliminar: "))

        elif opcion == '3':
            inv.actualizar_producto(input("Ingresa el ID del producto a actualizar: "))

        elif opcion == '4':
            inv.buscar_producto(input("Ingresa el nombre (o parte del nombre) a buscar: "))

        elif opcion == '5':
            inv.mostrar_inventario()

        elif opcion == '6':
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida. Por favor, elige un número del 1 al 6.")


if __name__ == "__main__":
    menu()
