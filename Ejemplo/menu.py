def menu():
    choice = 0
    print("===================================================")
    print("======G E S T I Ó N  D E  P R O D U C T O S========")
    print("===================================================")
    print("==")
    print("1. Añadir prodcuto")
    print("2. Mostras productos")
    print("3. Editar producto")
    print("4. ELiminar producto")
    print("5. Salir del programa\n")
    while True:
        try:
            choice = int(input("--> ¿Que desea hacer?")) 
            if choice not in range (1, 6):
                 print("no .")
            else: break
        except TypeError:   
            print("Su eleccion debe ser un numero...")
    return choice