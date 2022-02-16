term= int (input ("Enter Fibonacci Term ="))
fib = (0,1,1)
for i in range(term):
    fib = fib + ( fib [ i + 1] + fib [ i + 2 ],)
for j in range(len(fib)):
    if term == fib[ j ] :
        break
if j == len(fib)-1:
    print("Not Exist in Fibonacci Series ")
else :
    print("Fibonacci Series :- ", fib [ 0 :j +1] )
    print()
    print("This is ",j + 1,"th term of Fibonacci ")

    #BY VARUN GAUTAM (XI-A)
