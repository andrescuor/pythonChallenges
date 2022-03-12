db_products = {
    1:  ['Manzanas',   5000.0, 25],
    2:  ['Limones',    2300.0, 15],
    3:  ['Peras',      2700.0, 33],
    4:  ['Arandanos',  9300.0, 25],
    5:  ['Tomates',    2100.0, 42],
    6:  ['Fresas',     4100.0, 25],
    7:  ['Helado',     4500.0, 41],
    8:  ['Galletas',    500.0,  8],
    9:  ['Chocolates', 3500.0, 80],
    10: ['Jamon',     15000.0, 10]
}


#LEER
def read(bd, code):
    return bd.get(code)

#AGREGAR
def add(bd, code, value):
    bd[code] = value
    return bd

#ACTUALIZAR
def update(bd, code, value):
    bd.update({code: value})
    return bd

#BORRAR
def delete(bd, code):
    bd.pop(code)
    return bd

print("========================================")
print("| BIENVENIDO A LA TIENDA DE PEPE       |")
print("|          MENU                        |")
print("| 1. AGREGAR PRODUCTO                  |")
print("| 2. BORRAR PRODUCTO                   |")
print("| 3. ACTUALIZAR PRODCUTO               |")
print("| 4. VERIFICAR PRODCUTO                |")
print("| 5. ARROJAR INFORME                   |")
print("| 6. SALIR                             |")
print("| 7. ACTUALIZAR PRODCUTO               |")
print("========================================")
print("*POR FAVOR INGRESE LA OPCION A EJECUTAR*")

input_user = 0
while(input_user != 7):
    print("========================================")
    print("| BIENVENIDO A LA TIENDA DE PEPE       |")
    print("|          MENU                        |")
    print("| 1. AGREGAR PRODUCTO                  |")
    print("| 2. BORRAR PRODUCTO                   |")
    print("| 3. ACTUALIZAR PRODCUTO               |")
    print("| 4. VERIFICAR PRODCUTO                |")
    print("| 5. ARROJAR INFORME                   |")
    print("| 6. SALIR                             |")
    print("| 7. ACTUALIZAR PRODCUTO               |")
    print("========================================")
    print()
    input_user = input("*POR FAVOR INGRESE LA OPCION A EJECUTAR*")