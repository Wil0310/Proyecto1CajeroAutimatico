from datetime import datetime

# Datos simulados
pin_actual = "1234"
saldo = 1000.0
transacciones = []

# Función para registrar transacciones
def registrar_transaccion(tipo, monto=0):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if monto:
        transacciones.append(f"{fecha} - {tipo} - Q{monto:.2f}")
    else:
        transacciones.append(f"{fecha} - {tipo}")

# Validación de PIN
def login():
    intentos = 0
    while intentos < 3:
        ingreso = input("Ingrese su PIN: ")
        if ingreso == pin_actual:
            print("Acceso concedido")
            registrar_transaccion("Inicio de sesión")
            return True
        else:
            print("PIN incorrecto")
            intentos += 1
    print("Cuenta bloqueada por intentos fallidos")
    return False

# Consulta de saldo
def consultar_saldo():
    print(f"Su saldo actual es: Q{saldo:.2f}")
    registrar_transaccion("Consulta de saldo")

# Depósito
def depositar():
    global saldo
    try:
        monto = float(input("Ingrese monto a depositar: Q"))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: Q{saldo:.2f}")
            registrar_transaccion("Depósito", monto)
        else:
            print("Monto inválido")
    except ValueError:
        print("Entrada no válida")

# Retiro
def retirar():
    global saldo
    try:
        monto = float(input("Ingrese monto a retirar: Q"))
        if 0 < monto <= saldo:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: Q{saldo:.2f}")
            registrar_transaccion("Retiro", monto)
        else:
            print("Fondos insuficientes o monto inválido")
    except ValueError:
        print("Entrada no válida")

# Cambio de PIN
def cambiar_pin():
    global pin_actual
    nuevo = input("Ingrese nuevo PIN: ")
    confirmar = input("Confirme nuevo PIN: ")
    if nuevo == confirmar and len(nuevo) == 4 and nuevo.isdigit():
        pin_actual = nuevo
        print("PIN actualizado exitosamente")
        registrar_transaccion("Cambio de PIN")
    else:
        print("PIN inválido o no coincide")

# Ver historial de transacciones
def ver_transacciones():
    print("Historial de transacciones:")
    if transacciones:
        for t in transacciones:
            print(" -", t)
    else:
        print("No hay transacciones registradas.")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Cambiar PIN")
        print("5. Ver transacciones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            cambiar_pin()
        elif opcion == "5":
            ver_transacciones()
        elif opcion == "6":
            print("Gracias por usar el cajero. Hasta pronto.")
            registrar_transaccion("Cierre de sesión")
            break
        else:
            print("Opción inválida")

# Ejecución
if login():
    menu()