frutas = ("Manzana", "pera", "Uva", "Fresa")

fruta = iter(frutas)


print(next(fruta))
print(next(fruta))
print(next(fruta))
print(next(fruta))

#Produce un error cuando 
#se han recorrido todos
#los elementos y se intenta seguir iterando

#Reto: Itere una cadena de texto con iter() y next()


x = 5
y = "2"

try:
    result = x+y
    print (f"valor de x: {x}, valor de y {y}")
except TypeError:
    print("El valor de los sumandos ")


#Try except anidados
try:
    #Bloque externo
    try:
        #Bloque interno
        numero1 = int(input("Digite el primer numero:"))
        numero2 = int(input("Digite el segundo numero:"))
        resultado = numero1 / numero2
        print("El resultaado de la division es:", resultado)
    except ValueError:
        print("Algun numero tiene valor incorrecto")
    except ZeroDivisionError:
        print("NO se puede dividir por cero")
except Exception as e:
        print(e)        