# Parte 1 - Validación de PIN
pin = "1234"
intentos = 0
transacciones = []

def login():
    while intentos < 3:
        ingreso = input("Ingrese su PIN: ")
        if ingreso == pin:
            print("Acceso concedido")
            break
        else:
            print("PIN incorrecto")
            intentos + 1  # No se incrementa el contador