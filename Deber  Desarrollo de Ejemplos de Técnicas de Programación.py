# ============================================
#     Clase base: Vehículo
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Vehiculo)
# --------------------------------------------
# La abstracción se usa para representar únicamente lo esencial
# de un vehículo. En este ejemplo, la clase Vehiculo incluye solo
# los atributos básicos que definen cualquier vehículo:
# marca, modelo, año y tipo.
#
# La abstracción permite que esta clase sirva como modelo general
# para otras clases más específicas (como Auto o Moto),
# ocultando detalles innecesarios y enfocándose en lo importante.
# --------------------------------------------

class Vehiculo:
    def __init__(self, marca, modelo, ano, tipo):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Los atributos están protegidos usando un guion bajo,
        # lo que indica que no deben ser modificados directamente.
        #
        # Además, se utilizan métodos getters y setters para
        # controlar el acceso a estos datos. Esto permite:
        # Validar valores antes de asignarlos (ej: año > 1886)
        # Proteger la integridad de la información
        # Evitar cambios directos no controlados
        #
        # =====================================================
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._tipo = tipo

    # -------- MÉTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self._marca} {self._modelo} ({self._tipo}), {self._ano}"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_marca(self):
        return self._marca

    def set_marca(self, nueva_marca):
        if len(nueva_marca) > 1:
            self._marca = nueva_marca

    def get_ano(self):
        return self._ano

    def set_ano(self, nuevo_ano):
        if nuevo_ano > 1886:
            self._ano = nuevo_ano


# ============================================
#     HERENCIA: Auto y Moto
# ============================================

# ---------------------------------------------------------
# 3. HERENCIA (Auto y Moto heredan de Vehiculo)
# ---------------------------------------------------------
# La herencia permite crear nuevas clases basadas en una clase
# existente. En este ejemplo:
#
# • Auto(Vehiculo)
# • Moto(Vehiculo)
#
# Gracias a la herencia:
# Se reutilizan los atributos marca, modelo, año, tipo
# No es necesario reescribir código repetido
# Se agregan atributos propios: puertas y cilindrada
# Se puede expandir comportamiento sin duplicar código
# ---------------------------------------------------------

class Auto(Vehiculo):
    def __init__(self, marca, modelo, ano, tipo, puertas):
        # Llama al constructor de Vehiculo
        super().__init__(marca, modelo, ano, tipo)
        self._puertas = puertas

    # ---------------------------------------------
    # 4. POLIMORFISMO: método mostrar_info() redefinido
    # ---------------------------------------------
    # El polimorfismo permite que el mismo método (mostrar_info)
    # funcione diferente según el tipo de objeto.
    #
    # Aquí, Auto redefine mostrar_info() para incluir sus puertas.
    # ---------------------------------------------
    def mostrar_info(self):
        return (f"Auto: {self._marca} {self._modelo} ({self._tipo}), "
                f"{self._ano} - {self._puertas} puertas")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, ano, tipo, cilindrada):
        super().__init__(marca, modelo, ano, tipo)
        self._cilindrada = cilindrada

    # Polimorfismo nuevamente aplicado
    def mostrar_info(self):
        return (f"Moto: {self._marca} {self._modelo} ({self._tipo}), "
                f"{self._ano} - {self._cilindrada}cc")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

v1 = Vehiculo("Toyota", "Corolla", 2020, "Sedán")
a1 = Auto("Ford", "Mustang", 2023, "Deportivo", 2)
m1 = Moto("Honda", "CBR", 2022, "Deportiva", 600)

print(v1.mostrar_info())
print(a1.mostrar_info())  # ejemplo de polimorfismo
print(m1.mostrar_info())  # ejemplo de polimorfismo

# Usando encapsulación (modificando datos de forma controlada)
v1.set_marca("Toyota Actualizado")
v1.set_ano(2021)
print(v1.mostrar_info())
