## Problema 45: Calculadora con repetición por operación

print("=" * 60)
print("🖩 CALCULADORA CON REPETICIÓN POR OPERACIÓN 🖩".center(60))
print("=" * 60 + "\n")

continuar_programa = "si"

while continuar_programa.lower() == "si":
    
    
    print("\n" + "─" * 60)
    print(" OPERACIONES DISPONIBLES:")
    print("   1. Suma (+)")
    print("   2. Resta (-)")
    print("   3. Multiplicación (*)")
    print("   4. División (/)")
    print("   5. Exponente (**)")
    print("   6. Módulo (%)\n")
    
    try:
        opcion = int(input(" Selecciona una operación (1-6): "))
        
        if opcion < 1 or opcion > 6:
            print(" Opción no válida. Debe ser 1-6.")
            continue
        
        
        repetir_operacion = "si"
        
        while repetir_operacion.lower() == "si":
            
            print(f"\n--- OPERACIÓN SELECCIONADA3---")
            
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            print("\n" + "─" * 40)
            print("RESULTADO:")
            print("─" * 40)
            
            if opcion == 1:  
                resultado = num1 + num2
                print(f"   {num1} + {num2} = {resultado}")
                
            elif opcion == 2:  
                resultado = num1 - num2
                print(f"   {num1} - {num2} = {resultado}")
                
            elif opcion == 3: 
                resultado = num1 * num2
                print(f"   {num1} × {num2} = {resultado}")
                
            elif opcion == 4:  
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"   {num1} ÷ {num2} = {resultado}")
                else:
                    print("    Error: No se puede dividir entre cero")
                    
            elif opcion == 5:  
                resultado = num1 ** num2
                print(f"   {num1} ^ {num2} = {resultado}")
                
            elif opcion == 6:  
                if num2 != 0:
                    resultado = num1 % num2
                    print(f"   {num1} % {num2} = {resultado}")
                else:
                    print("    Error: No se puede calcular módulo con divisor cero")
            
            print("─" * 40)
            
            repetir_operacion = input("\n ¿Repetir la MISMA operación? (si/no): ")
            
        
        continuar_programa = input("\n ¿Deseas realizar OTRA operación distinta? (si/no): ")
        
    except ValueError:
        print(" Error: Debes ingresar números válidos")
        continue

print("\n" + "=" * 60)
print(" ¡Gracias por usar la calculadora!".center(60))
print("=" * 60)


def obtener_nombre_operacion(opcion):
    nombres = {
        1: "SUMA",
        2: "RESTA",
        3: "MULTIPLICACIÓN",
        4: "DIVISIÓN",
        5: "EXPONENTE",
        6: "MÓDULO"
    }
    return nombres.get(opcion, "DESCONOCIDA")