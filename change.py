def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input())
    print("Ingresar gasto:")
    print(gasto)
    dinero = int(input())
    print("Dinero recibido")
    print(dinero)

    vuelto = dinero - gasto
    print("")
    print("Vuelto")

    pesos =  int(vuelto)
    centavos = round((vuelto - pesos) * 100)
    print("")
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")
