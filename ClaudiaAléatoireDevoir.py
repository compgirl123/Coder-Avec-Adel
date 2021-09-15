numbers = []
number = 1
print("------------------------")
print("Programme Calculatrice")
print("------------------------")
print("SVP selectionner ce qu'on veut faire")
print("1 - Addition de deux numeros")
print("2 - Soustraction de deux numeros")
print("3 - Multiplication de deux numeros")
print("4 - Division de deux numeros")
print("5 - Power de deux numeros")
print("6 - Addition de cinqs numéros")
print("7 - Multipication de cinqs nombres")
print("8 - Soustraction de trois nombres")
print("9 - division de trois nombres")
selection_numero = input("Selection:")

if selection_numero == "1":
    n = input("number 1:")
    numbers.append(n)
    number += 1
    while n !="stop":
        n = input("number" + str(number) + ":")
        number += 1
        numbers.append(n)
    numbers.pop(-1)
    total_count = 0
    for x in numbers:
        variable = int(x)
        total_count += variable
    print(total_count)

elif selection_numero == "2":
    n = input("number 1:")
    numbers.append(n)
    number += 1
    while n !="stop":
        n = input("number" + str(number) + ":")
        number += 1
        numbers.append(n)
    numbers.pop(-1)
    total_count = 0
    for x in numbers:
        variable = int(x)
        total_count -= variable
    print(total_count)

elif selection_numero == "3":
    n = input("number 1:")
    numbers.append(n)
    number += 1
    while n !="stop":
        n = input("number" + str(number) + ":")
        number += 1
        numbers.append(n)
    numbers.pop(-1)
    total_count = 0
    for x in numbers:
        variable = int(x)
        total_count *= variable
    print(total_count)

elif selection_numero == "4":
    n = input("number 1:")
    numbers.append(n)
    number += 1
    while n !="stop":
        n = input("number" + str(number) + ":")
        number += 1
        numbers.append(n)
    numbers.pop(-1)
    total_count = 0
    for x in numbers:
        variable = int(x)
        total_count /= variable
    print(total_count)
