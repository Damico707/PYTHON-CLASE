opt = 0

productos = ["papa", "arroz", "yuca", "lenteja"]

def limpieza():
    input("Presione cualquier tecla para continuar...")
    os.system("clear")

while(True):
    print("1. Agregar producto\n2. Producto a editar\n3. Productos registrados\n4. Posicion productos\n5. Insetar elemntos en lista\n7. pop a un elemento\n8. Contar producto\n9. ordenar productos\n10. invertir lista\n11. Limpiar lista")
    opt = int(input("\n¿Que desea hacer?") or 0)
    match(opt):
        case 1:
            productos.append(input("Nombre del producto: "))
            print("Producto agregado....")
            input(".....")
        case 2:
            posc = int(input("Posición del producto"))
            print("Producto a editar: "+productos[posc])
            productos[posc] = input("Nuevo producto: ")
            print("Producto editado....")
            input(".....")
        case 3: 
            print(f"Productos registrados: {len(productos)}")
            input("...")
        case 4:
            posc = int(input("¿En que posicion agregar?"))
            prod = input ("Nombre del producto: ")
            productos.insert(posc, prod)
            print("Producto insertado")
        case 5:
            otrosProd = ["Detergente", True, 5000, ["campus", "trainer"]]
            productos.extend(otrosProd)
            print("Lista")
        case 6: 
            posc = input("Elemento a eliminar")
            productos.remove(prod)
            print("Producto eliminado")
        case 7:
            posc= int(input("Producto a eliminar"))
            print(f"Elemento eliminado: {productos.pop(posc)}")
        case 8:
            prod = input ("Nombre de prodcuto: ")
            print(f"EL producto  {prod} se repite {productos.count(prod)}")
        case 9:
            productos.sort()
            print("Productos ordenados...")
        case 10:
            productos.reverse()
            print("Lista de productos invertida...")
        case 11:
        prodcutos.clear()
        print("Lista vacia...")

    print(productos)
    if opt == 0: 
        print("bye bye")
        break
