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
question = 1
selection_numero = input("Selection:")
#def selection_validation():
  #  selection_numero = "0"
   # while(selection_numero != "arret"):
        
    #    numero_selection(selection_numero)  

def addition_two():
    while n1 !=stop:
        n1 = int(input("Enter Numero" + str(question)))
    answer = sum(n1)
    print(answer)
    return answer    

#def numero_selection(selection_numero):
 #   f = ""
if (selection_numero) == "1":
    addition_two()
elif int(selection_numero) == 2:
    subtraction_two()
elif int(selection_numero) == 3:
    multiplication_two()
elif int(selection_numero) == 4:
    division_two()
elif int(selection_numero) == 5:
    power_two()
else:
    f = "Invalid"
    #return f



def subtraction_two():
    n1 = int(input("Enter Numero 1:"))
    n2 = int(input("Enter Numero 2:"))
    subtraction = n1 - n2
    print(sum)
    return subtraction

def multiplication_two():
    n1 = int(input("Enter Numero 1:"))
    n2 = int(input("Enter Numero 2:"))
    mulitiplication = n1 * n2
    print(mulitiplication)
    return mulitiplication

def division_two():
    n1 = int(input("Enter Numero 1:"))
    n2 = int(input("Enter Numero 2:"))
    division = n1 / n2
    print(division)
    return division

'''def power_two():
    n1 = int(input("Enter Numero 1:"))
    n2 = int(input("Enter Numero 2:"))
    power = n1 ** n'''

def power_two():
    n1 = int(input("Enter Numero 1:"))
    n2 = int(input("Enter Numero 2:"))
    power = n1 ** n2
    print(power)
    return power

# A faire: toutes les options avec d'autres
#print(numero_selection())
#print(selection_validation())