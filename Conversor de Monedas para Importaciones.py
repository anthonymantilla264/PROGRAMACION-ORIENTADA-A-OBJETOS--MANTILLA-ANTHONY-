# Programa: Calculadora de Impuestos de Importación By Anthony Mantilla
# Descripción: Calcula impuestos y precio final de productos importados

def calcular_impuestos_importacion():
    """Calcula impuestos de importación y precio final"""

    print("=" * 50)
    print("CALCULADORA DE IMPUESTOS DE IMPORTACIÓN")
    print("=" * 50)

    # String: descripción del producto
    nombre_producto = input("\nNombre del producto: ")

    # Float: precio en dólares
    precio_usd = float(input("Precio en USD: $"))

    # Integer: porcentaje de impuesto (IVA + aranceles)
    porcentaje_impuesto = int(input("Porcentaje de impuestos (%): "))

    # Float: cálculo del impuesto
    monto_impuesto = precio_usd * (porcentaje_impuesto / 100)

    # Float: precio final
    precio_final = precio_usd + monto_impuesto

    # Boolean: ¿el producto supera los $400 USD?
    requiere_declaracion = precio_final > 400.0

    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESUMEN DE IMPORTACIÓN")
    print("=" * 50)
    print(f"Producto: {nombre_producto}")
    print(f"Precio base: ${precio_usd:.2f} USD")
    print(f"Impuestos ({porcentaje_impuesto}%): ${monto_impuesto:.2f} USD")
    print(f"Precio final: ${precio_final:.2f} USD")

    if requiere_declaracion:
        print("\n⚠ REQUIERE DECLARACIÓN ADUANERA (supera $400 USD)")
    else:
        print("\n✓ No requiere declaración aduanera")


# Ejecutar el programa
calcular_impuestos_importacion()
