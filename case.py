a=float(input("enter your first number"))
b=float(input("enter your second number"))
operation=input("enter your choice(+,-,/,*):")
if operation=="+":
    print("sum =", a+b)
elif operation=="-":
    print("sum =", a-b)
elif operation=="/":
    print("sum =", a/b)
elif operation=="*":
    print("sum =", a*b)
else:
    print("Invalid")