num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))
op = input("Enter the operation to perform \n")
if(op=="+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="*"):
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("Invalid operator")