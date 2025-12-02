print("python Calc.py")
number1 = input("enter the number:")
num1 = float(number1)
sign = input("enter the sign:")
number2 = input("enter the number:")
num2 = float(number2)
if sign == "+":
    print("your result is "+str(num1 + num2))
elif sign == "-":
    print("your result is "+str(num1 - num2))
elif sign == "*":
    print("your result is "+str(num1 * num2))
elif sign == "/":
    print("your result is "+str(num1 / num2))
elif sign == "//":
    print("your result is "+str(num1 // num2))
else:
    print("please enter +, -, *, / or // only:")
