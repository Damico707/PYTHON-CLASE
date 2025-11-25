
import os
opt = 0
productos = [{
            "code": "001",
            "name": "llantas",
            "price": "150000"
            },
            {

            "code": "002",
            "name": "espejos",
            "price": "120000"
            },
            {
            "code": "003",
            "name": "lubricante",
            "price": "80000"
            }
            ]

def limpieza():
   input("...")
   os.system("clear")
   os.system("cls" if os.name == "nt" else "clear")

def productIndex( code ):
    ind = -1
    for i in range(len(productos)):
        if productos[i]["code"] == code:
            ind = i
            break
    return ind
opt = 0

print(productos)
while(True):
    print("1. Agregar producto")
    opt = int(input("\n¿que desea hacer?>")or 0)
    match(opt):
        case 1:
            productos.append({
            "code" : input("Codigo del producto: "),
            "name": input("Nombre del producto: "),
            "price": input("Precio del producto: ")
        })
            print("producto agreagado..")
        case 2:
            code = input("Codigo de producto a modificar: ")
            prodInd = productIndex(code)
            if prodInd == -1:
                 print(f"producto con codigo {code} no existe.")
            else:
                print(f"codigo:{productos[prodInd].get('code')}")
                print(f"nombre:{productos[prodInd].get('name')}")
                print(f"precio:{productos[prodInd].get('price')}")
                print(f"activo:{productos[prodInd].get('active')}")
        case 3:
            producto = {
                "code": "001",
                "name": "llantas",
                "price": "150000"
            }
            #producto.clear()
            items = producto.item()
            print(items)
            for itm in items:
                print(itm)
            print(producto.keys())
            print(producto.values())
            keys= prodcuto.keys()
            for k in keys:
                print(f"{k} {producto[k]}")
    limpieza()

    print (productos)
    if opt==0:
        print("bye bye")
        break