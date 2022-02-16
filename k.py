lst = eval(input("Enter a list: "))
print("Existing list is:", lst)

n = int(input("Enter a number for increment: "))

for i in range(len(lst)):
    lst[i] += n

print("List after increment:", lst)

#BY VARUN GAUTAM (11-A)
