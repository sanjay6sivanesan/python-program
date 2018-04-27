number1 = float(input("enter the first number"))
number2 = float(input("enter the second number"))
number3 = float(input("enter the third number"))

if (number1 > number2) and (number1 > number3):
 biggest = num1
elif (number2 > number1) and (number2 > number3):
 biggest = number2
else:
 biggest = number3

print("The biggest number between",number1,",",number2,"and",number3,"is",biggest)
