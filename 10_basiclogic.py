a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a>b and a>c:
    print("Largest number is a: ", a)
elif b>a and b>c:
    print("Largest number is b: ",b)
else:
    print("Largest number is c:",c)