
categories= [{
            "code": "c001",
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

def productIndex( datalist, codeRef ):
    print(codeRef)
    ind = -1
    for i in range(len(datalist)):
        if datalist[i].get ("code") == codeRef:
            ind = i
            break
    return ind

def findproduct(categoryCode, productCode):
    catgIndex= findIndex(categories, categoryCode)
    if catgIndex == -1:
        print("categoria no existe...")
        return
    else:
        prodIndex = findIndex(categories[catgIndex]["products"], productCode)
        if prodIndex == -1:
            print("Producto no existe...")
        else:
            print(categories[catgIndex]["products"][prodIndex])

findproduct("c001", "002")