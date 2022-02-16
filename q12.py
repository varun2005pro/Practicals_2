tup = eval(input("Enter pair of tuples :-"))

count = 0
for  i in range (len(tup)):
    if tup [i][0] % 2 == 0 and tup[i][1] % 2 == 0:
        count += 1
print("The number of pair (a,b) such that a and b are even = ",count)

#BY VARUN GAUTAM(XI-A)
