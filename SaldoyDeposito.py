saldo = 1000  #Creación del saldo inicial

def consultar_saldo(): #Consulta el saldo existente en la cuenta
    print(f"Saldo actual: {saldo:.2f}")  

def depositar(): #Creación de la opción de deposito que nos permitira depositar en la cuenta
    try: #Try nos ayudara a hacer una corrección en cado caso el monto ingresado no sea tipo flotante
        monto = int(input("Monto a depositar: "))
    except ValueError:
        print("Porfavor, coloque un valor numerico, no textual")
    saldo += monto  
    print("¡Depósito exitoso!")