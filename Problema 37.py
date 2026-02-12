# Problema 37: Interés compuesto con repetición

print("=== CALCULADORA DE INTERÉS COMPUESTO ===\n")

continuar = "s"

while continuar == "s" or continuar == "si":
    
    print("-" * 40)
    C = float(input("Capital inicial ($): "))
    i = float(input("Tasa de interés anual (%): ")) / 100
    n = int(input("Número de periodos (años): "))
    
    M = C * (1 + i) ** n
    
    print("\n RESULTADO:")
    print(f"   Monto final: ${M:,.2f}")
    print(f"   Ganancia: ${M - C:,.2f}")
    print(f"   Crecimiento: {(M/C - 1) * 100:.1f}%")
    
    continuar = input("\n¿Deseas hacer otro cálculo? (s/n): ").lower()
    print()

print("¡Gracias por usar la calculadora!")