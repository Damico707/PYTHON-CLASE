def menu(title, options):
    choice = 0
    index =1
    print("===================================================")
    print(f"======{title}========")
    print("===================================================")
    print("==")
    for item in options:
        print(f"{index}. {item}")
        index += 1
    while True:
        try:
            choice = int(input("--> ¿Que desea hacer?")) 
            if choice not in range (1,len(options)+1):
                 print("no .")
            else: break
        except ValueError:   
            print("Su eleccion debe ser un numero...")
    return choice