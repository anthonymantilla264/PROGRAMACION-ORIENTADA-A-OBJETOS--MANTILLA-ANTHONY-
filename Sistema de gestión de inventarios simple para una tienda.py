class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self): return self.id_producto

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    # Setters
    def set_nombre(self, nombre): self.nombre = nombre

    def set_cantidad(self, cantidad): self.cantidad = cantidad

    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"[{self.id_producto}] {self.nombre} - Cantidad: {self.cantidad} - Precio: ${self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                nueva_cant = input("Nueva cantidad (Enter para omitir): ")
                nuevo_precio = input("Nuevo precio (Enter para omitir): ")

                if nueva_cant: p.set_cantidad(int(nueva_cant))
                if nuevo_precio: p.set_precio(float(nuevo_precio))

                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = False
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrados = True
        if not encontrados:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)


def menu():
    inv = Inventario()

    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Mostrar | 6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_p = input("ID: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            inv.añadir_producto(Producto(id_p, nom, cant, pre))

        elif opcion == '2':
            inv.eliminar_producto(input("ID a eliminar: "))

        elif opcion == '3':
            inv.actualizar_producto(input("ID a actualizar: "))

        elif opcion == '4':
            inv.buscar_producto(input("Nombre a buscar: "))

        elif opcion == '5':
            inv.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
