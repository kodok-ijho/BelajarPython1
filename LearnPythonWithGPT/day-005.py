def find_max(a, b):
    if a > b:
        return a
    else:
        return b


a=input("Input first number : ")
b=input("Input second number : ")
c=input("Input third number : ")

x=find_max(a, find_max(b,c))
print("The large number is :"+str(x))