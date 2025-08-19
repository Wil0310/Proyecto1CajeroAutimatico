saldo = 1000  #Creación del saldo inicial

def consultar_saldo(): #Consulta el saldo existente en la cuenta
    print(f"Saldo actual: {saldo:.2f}")  

def depositar(): 
    try:
        monto = int(input("Monto a depositar: "))
    except ValueError:
        print("Porfavor, coloque un valor numerico, no textual")
    saldo += monto  
    print("¡Depósito exitoso!")