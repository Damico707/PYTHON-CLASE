from menu import menu
from jsonFileHandler import *
from Ejemplo.utilListas import *

PRODUCT_FILE_PATH = "./Database/products.json"
options = ("añadir producto",
"mostras producto",
"Editar productos",
"Eliminar producto",
"Buscar producto",
"salir del programa")

while True:
    choice = menu("G E S T I O N  D E  P R O D U C T O S", options)
    match choice:
        case 1:
            product = {
                "code" : input("Ingrese codigo del producto: "),
                "name" : input("Ingrese el nombre del producto "),
                "price": int(input("Ingrese precio del producto: ")),
                "provider": (input("Ingrese el proveedor del producto: ")),
                "active": True
            }

            dataProducts= readFile(PRODUCT_FILE_PATH)
            dataProducts.append(product)
            saveFile(PRODUCT_FILE_PATH, dataProducts)
        case 2:
            products = readFile(PRODUCT_FILE_PATH)
            if len(products)== 0:
                print("No hay productos registrados...")
            else:
                print("=== P R O D U C T O S   R E G I S T R A D O S ===")
                print("= CODIGO  NOMBRE            PROVEEDOR           PRECIO       ESTADO====\n")
                for product in products:
                    print(f"  {product ['code']:<8}  {product ['name']:<19} {product['provider']:<18} {product ['price']:<12} {'Activo' if product['active'] else 'Inactivo':<10}==")
        case 3:
            productCode = input("Codigo del producto a editar: ")
            products = readFile(PRODUCT_FILE_PATH)
            info = finDictionary(products, "code", productCode)
            if len(indo.keys())
                print("Codigo no encontrado...")
            else:
                editProd = {
                    "name": input("nuevo nombre") or infor["data"]["name"]
                }
                print(editProd)
        case 4:
            productCode = input("Codigo del producto a editar: ")
            products = readFile(PRODUCT_FILE_PATH)
            info = finDictionary(products, "code", productCode)
            print(f"Desea borrar el producto {info['data']['code']} - {info['data']['code']}  (S/N)?: ")
        case 6:
            print("bye")
            break
