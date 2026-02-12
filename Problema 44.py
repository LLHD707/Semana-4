## Problema 44: Calcular básica con repetición

print("=" * 50)
print("🖩 CALCULADORA BÁSICA 🖩".center(50))
print("=" * 50 + "\n")


continuar = "si"

while continuar.lower() == "si":
    
    
    print("\n--- OPERACIONES DISPONIBLES ---")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Exponente (**)")
    print("6. Módulo/Residuo (%)\n")
    
    
    try:
        opcion = int(input("Selecciona una operación (1-6): "))
        
        
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print("\n" + "-" * 40)
        print("RESULTADO:")
        print("-" * 40)
        
        
        if opcion == 1:  
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
            
        elif opcion == 2:  
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
            
        elif opcion == 3:  
            resultado = num1 * num2
            print(f"{num1} × {num2} = {resultado}")
            
        elif opcion == 4:  
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} ÷ {num2} = {resultado}")
            else:
                print(" Error: No se puede dividir entre cero")
            
        elif opcion == 5:  
            resultado = num1 ** num2
            print(f"{num1} ^ {num2} = {resultado}")
            
        elif opcion == 6:  
            if num2 != 0:
                resultado = num1 % num2
                print(f"{num1} % {num2} = {resultado}")
            else:
                print(" Error: No se puede calcular módulo con divisor cero")
                
        else:
            print(" Opción no válida. Debes seleccionar 1-6.")
            
    except ValueError:
        print(" Error: Debes ingresar números válidos")
    
    print("-" * 40)
    
    
    continuar = input("\n¿Deseas realizar otra operación? (si/no): ")

print("\n" + "=" * 50)
print("👋 ¡Gracias por usar la calculadora!".center(50))
print("=" * 50)