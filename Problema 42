##Problema 43: Acumulafor de abonos

print("=== CONFIRMACIÓN DE CONTRASEÑA (3 INTENTOS) ===\n")

contrasena = input("Ingresa tu contraseña: ")

print("\nConfirma tu contraseña. Tienes 3 intentos.")

intentos = 0
confirmacion = ""
limite = 3

while confirmacion != contrasena and intentos < limite:
    intentos += 1
    confirmacion = input(f"Intento #{intentos}/{limite}: Vuelve a ingresar tu contraseña: ")
    
    if confirmacion == contrasena:
        print("\n✅ ¡Contraseña confirmada correctamente!")
    else:
        intentos_restantes = limite - intentos
        if intentos_restantes > 0:
            print(f"❌ No coinciden. Te quedan {intentos_restantes} intento(s).\n")

if confirmacion != contrasena:
    print("\n🚫 CUENTA CANCELADA - Has excedido el número de intentos.")