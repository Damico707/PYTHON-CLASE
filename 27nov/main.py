import papota

print(f"la suma es: {papota.sumar(5, 3, 10)}")

#importa parte del modulo:
from papota import restar
print (f"La resa es: {restar(2, 10)}")


#importar mas de una
#funcion del modulo:

from papota import sumar, restar
print(f"la suma es: {sumar(5,3)}")
print(f"la resta es: {restar (2,10)}")

#otra forma de importar
#todo del modulo:
from papota import*
print(f"la suma es: {sumar(5,3)}")
print(f"la resta es: {restar(2,10)}")
print(f"la multiplicacion es: {multiplicar(3,3)}")
print(f"la division es: {dividir(12,3)}")

#importar modulos con
#una carpeta contigua

from util.saludar import saludar
saludar()

#Agregarle un alias a
#lo que estamos importando:
from papota import restar as sustraccion
print(f"la resta es: {sustraccion(9,6)}")