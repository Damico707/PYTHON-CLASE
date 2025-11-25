contador_platos = 0
contador_bebidas = 0
contador_adicionales = 0

def menuplatos():
    global contador_platos
    print("====PLATILLOS====")
    print("1. Albondigas / 12.000")
    print("2. Gordon blue / 15.000")
    print("3. Pastas mixtas / 14.000")

    comidita = int(input("-> "))

    if comidita in (1,2,3):
        print("Platillo agregado.")
        contador_platos += 1
    else:
        print("Opción no válida.")

def menubebidas():
    global contador_bebidas
    print("====BEBIDAS====")
    print("1. Limonada natural / 2.000")
    print("2. Coca cola personal / 3.000")
    print("3. Jugo natural / 6.000")

    bebida = int(input("-> "))

    if bebida in (1,2,3):
        print("Bebida agregada.")
        contador_bebidas += 1
    else:
        print("Opción no válida.")

def adicionales():
    global contador_adicionales
    print("====ADICIONALES====")
    print("1. Proteína / 7.000")
    print("2. Aguacate / 4.000")
    print("3. Sopa extra / 2.000")

    adicion = int(input("-> "))

    if adicion in (1,2,3):
        print("Adicional agregado.")
        contador_adicionales += 1
    else:
        print("Opción no válida.")

def principal():
    while True:
        print("\n=== BIENVENIDO A SANTORINI ===")
        print("1. Platos del día")
        print("2. Bebidas")
        print("3. Adicionales")
        print("4. Finalizar y ver recibo")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            menuplatos()
        elif op == 2:
            menubebidas()
        elif op == 3:
            adicionales()
        elif op == 4:
            break
        else:
            print("Opción inválida\n")
    print("\n===== RECIBO FINAL =====")
    print("Platos seleccionados:", contador_platos)
    print("Bebidas seleccionadas:", contador_bebidas)
    print("Adicionales seleccionados:", contador_adicionales)
    print("TOTAL DE PRODUCTOS:", contador_platos + contador_bebidas + contador_adicionales)
    print("========================")


principal()