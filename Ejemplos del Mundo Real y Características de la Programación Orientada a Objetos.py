"""
Sistema Aduanero Simple POO Mundo Real
Demuestra: Clases, Herencia, Polimorfismo, Encapsulación
"""
class Producto:
    """Clase base para productos aduaneros"""
    def __init__(self, nombre, valor, pais):
        self._nombre = nombre  # Encapsulamiento
        self._valor = valor
        self._pais = pais
        self._cantidad = 0
    def agregar(self, cantidad):
        self._cantidad += cantidad
    def mostrar(self):
        return f"{self._nombre} ({self._pais}): ${self._valor * self._cantidad:.2f}"
class ProductoPeligroso(Producto):
    """Herencia: productos con restricciones"""
    def __init__(self, nombre, valor, pais, peligro):
        super().__init__(nombre, valor, pais)
        self._peligro = peligro
    def mostrar(self):  # Polimorfismo
        return f"️ {super().mostrar()} - Peligro: {self._peligro}"
class Contenedor:
    """Agrupa productos para envío"""
    def __init__(self, numero):
        self._numero = numero
        self.productos = []
    def agregar_producto(self, producto):
        producto.agregar(10)  # Cantidad fija
        self.productos.append(producto)
    def mostrar_todo(self):
        print(f"\n=== CONTENEDOR {self._numero} ===")
        for p in self.productos:
            print(p.mostrar())  # Polimorfismo en acción
        print("=========Anthony Mantilla===========\n")

# Visualizador
contenedor = Contenedor("CNTR-001")

# Crear objetos e interactuar
normal = Producto("Celulares", 200, "China")
peligroso = ProductoPeligroso("Químicos", 500, "Alemania", "Alto")

contenedor.agregar_producto(normal)
contenedor.agregar_producto(peligroso)

contenedor.mostrar_todo()