## Problema 43: Acumulador de abonos

print("=== ACUMULADOR DE ABONOS ===\n")
print("Objetivo: Acumular $100,000 en abonos\n")


total_acumulado = 0
objetivo = 100000

while total_acumulado < objetivo:
    
    
    print(f" Total acumulado: ${total_acumulado:,.2f}")
    print(f" Meta: ${objetivo:,.2f}")
    print(f" Faltan: ${objetivo - total_acumulado:,.2f}\n")
    
    
    try:
        abono = float(input("¿Cantidad a abonar? $"))
        
        
        if abono < 0:
            print(" Error: No se aceptan cantidades negativas. Intenta de nuevo.\n")
        else:
            
            total_acumulado += abono
            print(f" Abono de ${abono:,.2f} registrado correctamente.\n")
            
    except ValueError:
        print(" Error: Debes ingresar un número válido.\n")


print("\n" + "=" * 50)
print(" ¡META ALCANZADA! ".center(50))
print("=" * 50)
print(f" Total acumulado: ${total_acumulado:,.2f}")
print(f" Meta: ${objetivo:,.2f}")
print(f" Excedente: ${total_acumulado - objetivo:,.2f}")
print("=" * 50)