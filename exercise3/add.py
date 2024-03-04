#a = int(input("Enter a number: "))
#b = int(input("Enter another number to be added to the first: "))
#print("The sum of these numbers is " + str(a + b))

#age = int(input("Enter your age: "))
#print("Age between 18 and 35: " + str(18 < age < 35))


a = int(input("please enter a number: "))
b = int(input("please enter a number: "))
operator = input("please enter an operator (+ or -): " )

if operator == "+":
    print("Your answer is: " + str(a + b))

elif operator == "-":
     print("Your answer is: " + str(a - b))

else:
    print("unknown operator")



