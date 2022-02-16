dict={}
ch='y'
while ch=='y' or ch=='Y':
    name=input("Enter name of product : ")
    price=eval(input("Enter the price of product : "))
    dict[name]=price
    ch=input("Want to add more items (Y/N) : ")
print(dict)

#VARUN GAUTAM (XI-A)
