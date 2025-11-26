from csv import reader, writer

# Funcion Reader
with open ("a.csv", "r") as file:
    lector = reader(file)
    for row in lector:
        print(row)

#Funcion Writer
myData = [
    ["firstName", "Secondname","Grade"],
    ["Alex", "Goodoy", "2"],
    ["Carlos", "De la torre", "2"]
]

myfile = open("personas.csv", "w", newline= '')
with myFile:
    escritor= write(myFile)
    escritor.writerows(myData)

#Funcion DictReader -> escribir diccionarios. Toma la primera linea
#como encabezado de cada columna

with open('ventas_semana_pasada.csv') as f:
    DictReader_obj = DictReader(f)
    for item in DictReader_obj:
        print(item['DIA']): {item['JORDANA1']}")

def write_reservations(f, reservations, headers)
with (f, "w", newline='')as f2:
    writer = DictWriter(f2, fieldnames = headers)
    if headers:
        writer.writeheader()
    for reservation in reservation
        writer.writerow({
            'availability zone': reservation["availability_zone"]
            'tenancy': reservation ["tenancy"],
            'product': reservation["product"],
            'cost_hourly': reservation["cost_upfront"],
            'count used': reservation ["count_used"],

        })

headers = [
        'availability zone',
        'tenancy',
        'product',
        'cost_hourly'
        'cost_upfront
        'count'
]