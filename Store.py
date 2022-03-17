bd_products = {
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


# LEER
def read(bd, code):
    return bd.get(code)


# Add
def add(bd):
    code = input('Please insert the code of the product: ')
    product_name = input('Please insert the name of the product: ')
    product_price = input('Please insert the prince of the product: ')
    product_quantity = input('Please insert the current quantity of the product: ')
    bd[code] = [product_name, product_price, product_quantity]
    return bd


# Update
def update(bd):
    code = input('Please insert the code of the product')
    product_name = input('Please insert the name of the product')
    product_price = input('Please insert the prince of the product')
    product_quantity = input('Please insert the current quantity of the product')
    bd.update({code: [product_name, product_price, product_quantity]})
    return bd


# Delete
def delete(bd, code):
    bd.pop(code)
    return bd


# Print DB
def bd_print(bd):
    for key,value in bd.items():
        print('ID:', key, 'Product:', value[0], ', Price:', value[1], ', Quantity:', value[2])


# Print Menu
def menu():
    print("========================================")
    print("|        WELCOME TO THE STORE          |")
    print("|                 MENU                 |")
    print("| 1. ADD PRODUCT                       |")
    print("| 2. DELETE PRODUCT                    |")
    print("| 3. UPDATE PRODUCT                    |")
    print("| 4. VERIFY PRODUCT                    |")
    print("| 5. MAKE A REPORT                     |")
    print("| 6. SHOW THE CURRENT DB               |")
    print("| 6. EXIT                              |")
    print("========================================")
    input_user = int(input("Please select an option, an then press enter: "))
    if (input_user == 1):
        add(bd_products)
        menu()
    elif(input_user == 2):
        pass
    elif(input_user == 3):
        update(bd_products)
        menu()
    elif(input_user == 4):
        pass
    elif(input_user == 5):
        pass
    elif(input_user == 6):
        bd_print(bd_products)
        menu()
    elif(input_user == 0):
        exit()


if __name__ == "__main__":
    menu()
