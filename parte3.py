# Parte 3 - Retiro y transacciones
def retirar():
    monto = input("Monto a retirar: ")
    if monto < saldo:  # Comparación inválida
        saldo = saldo - monto  # Tipos incompatibles
        transacciones.append("Retiro de " + monto)
        print("Retiro exitoso")
    else:
        print("Fondos insuficientes")

def ver_transacciones():
    print("Historial:")
    for t in transacciones:
        print(t)