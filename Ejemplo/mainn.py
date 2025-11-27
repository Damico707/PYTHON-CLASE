from menu import menu
from jsonFileHandler import *

PRODUCT_FILE_PATH = "./Database/products.json"

while True:
    choice = menu()
    print(f"El usuario eligio la opcion: {choice}")
    match choice:
        case 1:
            product = {
                "code" : input("Ingrese codigo del producto: "),
                "name" : input("Ingrese el nombre del producto "),
                "price": int(input("Ingrese precio del producto: ")),
                "active": True
           }

            dataProducts= readFile(PRODUCT_FILE_PATH)
            dataProducts.append(product)
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 2:
            readFile(PRODUCT_FILE_PATH)
        case 4:
            
        case 5:
            print("bye")
            break
