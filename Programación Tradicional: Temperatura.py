def entrada_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Valida que sean números válidos y retorna una lista.
    """
    temperaturas = []
    for dia in range(1, 8):  # 7 días de la semana
        while True:
            try:
                valor = float(input(f"Ingrese la temperatura del día {dia} en °C: "))
                temperaturas.append(valor)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    return temperaturas

def calcular_promedio(semanal):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna 0.0 si la lista está vacía.
    """
    if not semanal:
        return 0.0
    return sum(semanal) / len(semanal)

def imprimir_resultado(promedio):
    """
    Muestra el promedio semanal con formato de 2 decimales.
    """
    print(f"\n{'='*40}")
    print(f"Promedio semanal de temperaturas: {promedio:.2f} °C")
    print(f"{'='*40}")

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("=== CÁLCULO DE PROMEDIO SEMANAL DE TEMPERATURAS ===")
    temperaturas_semana = entrada_temperaturas_diarias()
    promedio = calcular_promedio(temperaturas_semana)
    imprimir_resultado(promedio)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
