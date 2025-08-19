saldo = 1000  #Creación del saldo inicial

def consultar_saldo(): #Consulta el saldo existente en la cuenta
    print(f"Saldo actual: {saldo:.2f}")  

def depositar(): 
    monto = int(input("Monto a depositar: "))
    saldo += monto  
    print("¡Depósito exitoso!")