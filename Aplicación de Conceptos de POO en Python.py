# Sistema de Gestión de Vehículos - Programa POO Simplificado

class Vehiculo:
    """
    Clase base que representa un vehículo.
    Demuestra encapsulación con atributos protegidos.
    """
    def __init__(self, marca, modelo, año):
        self._marca = marca  # Atributo encapsulado
        self._modelo = modelo
        self._año = año
        self.__kilometraje = 0  # Atributo privado

    # Métodos getter (encapsulación)
    def get_marca(self):
        return self._marca

    def get_info(self):
        return self.__kilometraje

    # Método que será sobrescrito (polimorfismo)
    def arrancar(self):
        return f"El vehículo {self._marca} {self._modelo} está arrancando..."

    def mostrar_datos(self):
        return f"{self._marca} {self._modelo} ({self._año})"

    # Polimorfismo con argumentos variables
    def calcular_costo_viaje(self, kilometros, precio_combustible=2.5):
        consumo = kilometros * 0.08  # 0.08 litros por km
        costo = consumo * precio_combustible
        return costo


class Auto(Vehiculo):
    """
    Clase derivada que hereda de Vehiculo.
    Representa un automóvil con características específicas.
    """

    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)  # Herencia
        self._num_puertas = num_puertas

    # Sobrescritura de método (polimorfismo)
    def arrancar(self):
        return f"El auto {self._marca} {self._modelo} con {self._num_puertas} puertas está listo para conducir."

    def mostrar_datos(self):
        return f"{self._marca} {self._modelo} ({self._año}) - {self._num_puertas} puertas"


class Moto(Vehiculo):
    """
    Clase derivada que hereda de Vehiculo.
    Representa una motocicleta.
    """

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)  # Herencia
        self._cilindrada = cilindrada

    # Sobrescritura de método (polimorfismo)
    def arrancar(self):
        return f"La moto {self._marca} {self._modelo} de {self._cilindrada}cc está rugiendo."

    def mostrar_datos(self):
        return f"{self._marca} {self._modelo} ({self._año}) - {self._cilindrada}cc"

    # Las motos consumen menos combustible
    def calcular_costo_viaje(self, kilometros, precio_combustible=2.5):
        consumo = kilometros * 0.04  # Motos consumen menos
        costo = consumo * precio_combustible
        return costo


# Demostración del programa
print("=" * 60)
print("SISTEMA DE GESTIÓN DE VEHÍCULOS")
print("=" * 60)

# Crear objetos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
auto1 = Auto("Honda", "Civic", 2022, 4)
moto1 = Moto("Yamaha", "R15", 2023, 155)

print("\n--- ENCAPSULACIÓN ---")
print(f"Marca del vehículo: {vehiculo1.get_marca()}")

print("\n--- HERENCIA ---")
print("Auto hereda de Vehiculo:")
print(auto1.mostrar_datos())
print("Moto hereda de Vehiculo:")
print(moto1.mostrar_datos())

print("\n--- POLIMORFISMO (Sobrescritura) ---")
print(vehiculo1.arrancar())
print(auto1.arrancar())
print(moto1.arrancar())

print("\n--- POLIMORFISMO (Argumentos variables) ---")
print(f"Costo de viaje de 100 km en auto: ${auto1.calcular_costo_viaje(100):.2f}")
print(f"Costo con combustible a $3.0: ${auto1.calcular_costo_viaje(100, 3.0):.2f}")
print(f"Costo de viaje de 100 km en moto: ${moto1.calcular_costo_viaje(100):.2f}")

print("\n" + "=" * 60)