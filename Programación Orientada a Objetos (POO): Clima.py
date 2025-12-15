class ClimaDiario:
    """
    Clase base que representa la información climática de un solo día.
    Encapsula fecha y temperatura con propiedades protegidas.
    """

    def __init__(self, fecha=None, temperatura=None):
        self._fecha = fecha
        self._temperatura = temperatura

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if isinstance(valor, (int, float)):
            self._temperatura = float(valor)
        else:
            raise ValueError("La temperatura debe ser un número")

    def ingresar_temperatura(self):
        """Método para ingresar temperatura interactivamente"""
        while True:
            try:
                valor = float(input(f"Ingrese temperatura en °C: "))
                self.temperatura = valor
                break
            except ValueError:
                print("Error: Ingrese un número válido.")


class ClimaSemanal(ClimaDiario):
    """
    Clase hija que gestiona una semana completa de temperaturas.
    Herencia de ClimaDiario + métodos para semana completa.
    """

    def __init__(self, nombre_semana="Semana Actual"):
        super().__init__()
        self._nombre_semana = nombre_semana
        self._dias = []

    @property
    def nombre_semana(self):
        return self._nombre_semana

    def agregar_dia(self, dia):
        """Agrega un día válido a la semana"""
        if isinstance(dia, ClimaDiario):
            self._dias.append(dia)
        else:
            raise TypeError("Solo se permiten objetos ClimaDiario")

    def ingresar_temperaturas_semana(self):
        """
        Ingresa interactivamente las 7 temperaturas de la semana.
        Utiliza polimorfismo al llamar al método de la clase base.
        """
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves",
                       "Viernes", "Sábado", "Domingo"]

        print(f"\n--- Ingrese temperaturas para {self.nombre_semana} ---")
        for dia_nombre in dias_semana:
            dia = ClimaDiario(fecha=dia_nombre)
            dia.ingresar_temperatura()
            self.agregar_dia(dia)
            print(f"✓ {dia_nombre}: {dia.temperatura:.1f}°C registrado")

    def promedio_semanal(self):
        """Calcula y retorna el promedio semanal"""
        if not self._dias:
            return 0.0
        total = sum(dia.temperatura for dia in self._dias)
        return total / len(self._dias)

    def mostrar_resumen(self):
        """Muestra resumen completo de la semana"""
        if not self._dias:
            print("No hay datos de temperatura.")
            return

        print(f"\n{'=' * 50}")
        print(f"RESUMEN - {self.nombre_semana}")
        print(f"{'=' * 50}")

        for dia in self._dias:
            print(f"{dia.fecha:12}: {dia.temperatura:6.1f}°C")

        promedio = self.promedio_semanal()
        print(f"{'-' * 50}")
        print(f"{'PROMEDIO SEMANAL:':<25} {promedio:6.2f}°C")
        print(f"{'=' * 50}")


def main():
    """Función principal del programa POO"""
    print("🌡️  SISTEMA DE CLIMA SEMANAL - PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 60)

    # Crear instancia de la clase principal
    semana = ClimaSemanal("Semana del 14-Diciembre-2025")

    # Ingresar datos usando POO
    semana.ingresar_temperaturas_semana()

    # Mostrar resultados
    semana.mostrar_resumen()


# Punto de entrada
if __name__ == "__main__":
    main()

2