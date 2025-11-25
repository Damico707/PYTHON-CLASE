import os 
ops = 0
productos=[]
productos= {"code": "001", "name": "lapiz", "price":1200, "active": True}

client = {
    "identification": "X00014",
    "name": "John doe",
    "age": 28,
    "location": {
        "city": "Bucaramanga",
        "addres": "cr21 #35-9"
        },
    "favoriteMusic": [ "Vallenato", "Merengue", "Bolero", "Salsa"],
    "references": ( "x0005646", "x351646")
}

diccionario2 =dict(
    [
        ("nombre", "john"),
        ("edad", 28),
        ("esEstudiante", False)
    ]
)
print(diccionario2)

def limpieza():
    INPUT("...")
    os.system("cls" if os.name == "nt" else "clear")

while(True):
    print("1. Agregar producto")
    opt = int(input("\n¿Que desea hacer?>") or 0)
    match(opt):
        case 1:
            print(producto)
            input("producto agregado")

    limpieza()

    print(productos)
    if opt== 0:
        print("bye bye")
        break