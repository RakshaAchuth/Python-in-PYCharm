number1 = int(input("enter 1:"))
number2 = int(input("enter 2:"))
print("Add")
print("sub")
print("Div")
print("mul")
choice = int(input("chose ope:"))

print(number1+number2)
print (choice)

if choice == 1:
    result = number1 + number2
    print(number1 + number2)
elif choice == 2:
    result = number1 - number2
    print (number1 -number2)
elif choice == 3:
    result = number1 / number2
    print(number1/number2)
elif choice==4:
    result = number1 * number2
    print (number1 * number2)
else:
    result = "invalid choice"
    print ("invalid choice")
