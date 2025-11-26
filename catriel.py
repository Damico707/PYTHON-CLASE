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
        'count_used',
        ]
reservations = [
    {"availability_zone": 2,
        "tenancy": 3,
        'product':1,
        'cost_hourly': 3500,
        'cost_upfront': 4800,
        "count": 45,
        "count_used":1
    },{"availability_zone": 3,
        "tenancy": 3,
        'product': 4,
        'cost_hourly': 3700
        'cost_upfront': 5800,
        "count": 25,
        "count_used":13

    }]      
write_reservations("reservations.csv", reservations, headers)