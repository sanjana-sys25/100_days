print ("This is a simple calculator")
x=float(input("enter the first value"))
y=float(input("enter the second value"))
op=input("enter the operation you want to perform (+, -, *, /): ")
if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="*":
    print(x*y)
elif op=="/":
    print(x/y)
else:
    print("Invalid operation")