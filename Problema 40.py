#Problema 40: Repetición hasta respuesta específica

print("=== PROGRAMA DE CONFIRMACIÓN ===\n")

respuesta = "si"  # Inicializamos para que entre al ciclo

while respuesta.lower() == "si":
    print(" El programa sigue ejecutándose...")
    respuesta = input("¿Deseas continuar? (si/no): ")

print("\n Programa terminado. ¡Hasta luego!")