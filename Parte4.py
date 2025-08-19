
# Parte 4 - Cambio de PIN
def cambiar_pin():
    nuevo = input("Nuevo PIN: ")
    pin = nuevo  # No usa global
    transacciones.append("Cambio de PIN")
    print("PIN actualizado")