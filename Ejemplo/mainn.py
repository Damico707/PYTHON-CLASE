from menu import menu

while True:
    choice = menu()

    print(f"El usuario eligio la opcion: {choice}")
    match choice:
        case 5:
            print("bye")
            break